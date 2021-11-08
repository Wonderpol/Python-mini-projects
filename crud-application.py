import mysql.connector
from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
import jsonpickle


def connect_to_database() -> mysql.connector.connection:
    connection = mysql.connector.connect(
        user='root',
        password='password',
        host='127.0.0.1',
        database='python',
        auth_plugin='mysql_native_password')

    return connection


class User:
    def __init__(self, userid, username, city):
        self.userid = userid
        self.username = username
        self.city = city


app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_users():
    users: list = []
    connection = connect_to_database()
    cursor = connection.cursor(dictionary=True)
    query = 'SELECT id, username, city FROM users'
    cursor.execute(query)

    for raw in cursor:
        users.append(User(raw['id'], raw['username'], raw['city']))

    connection.close()

    return Response(jsonpickle.encode(users, unpicklable=False), mimetype='application/json')


@app.route('/users', methods=['POST'])
def add_user():
    request_data = request.get_json()
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        query = 'INSERT INTO users(username, city) VALUES(%(username)s, %(city)s)'
        cursor.execute(query, request_data)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify(details=err.msg), 400
    finally:
        connection.close()

    return request_data, 201


@app.route('/users/<user_id>', methods=['PUT'])
def edit_user(user_id):
    request_data = request.get_json()
    request_data['user_id'] = user_id
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        query = 'UPDATE users SET username=%(username)s, city=%(city)s WHERE id=%(user_id)s'
        cursor.execute(query, request_data)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify(details=err.msg), 400
    finally:
        connection.close()

    return request_data


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    request_data = {'user_id': user_id}
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        query = 'DELETE FROM users WHERE id=%(user_id)s'
        cursor.execute(query, request_data)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify(details=err.msg), 400
    finally:
        connection.close()

    return jsonify()


app.run()
