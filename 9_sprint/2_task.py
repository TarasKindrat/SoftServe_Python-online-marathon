"""
Create class  Users{
id -> int (unique)
username	->string
firstName	-> string
lastName -> string
email -> string
password	-> string
}
implement the class SimpleHTTPRequestHandler(BaseHTTPRequestHandler)
which will have overloaded methods for CRUD of operations with the user
=======================================================================
GET /reset
Parameters: No parameters
responses code 204

this method reset USERS_LIST to the

 [

            {

                "id": 1,

                "username": "theUser",

                "firstName": "John",

                "lastName": "James",

                "email": "john@email.com",

                "password": "12345",

            }

        ]

 which is the default for server startup
=======================================================================
POST 	/user	Create user
Parameters: No parameters
Request body:
{
  "id": 1,
  "username": "theUser",
  "firstName": "John",
  "lastName": "James",
  "email": "john@email.com",
  "password": "12345",
}
Responses:
code: 201
Response body:  {
  "id": 1,
  "username": "theUser",
  "firstName": "John",
  "lastName": "James",
  "email": "john@email.com",
  "password": "12345",
}

code: 400
Response body: {}
=======================================================================
POST	/user/createWithList	Creates list of users with given input array
Parameters: No parameters
Request body:
[
  {
    "id": 1,
    "username": "theUser",
    "firstName": "John",
    "lastName": "James",
    "email": "john@email.com",
    "password": "12345",
  }
]
Responses:
code: 201
Response body:
{
  "id": 1,
  "username": "theUser",
  "firstName": "John",
  "lastName": "James",
  "email": "john@email.com",
  "password": "12345",
}

code: 400
Response body: {}
=======================================================================
GET	/uses	Get all users
Parameters: No parameters
Responses:
satus 200
Request body:
[
  {
    "id": 1,
    "username": "theUser",
    "firstName": "John",
    "lastName": "James",
    "email": "john@email.com",
    "password": "12345",
  }
]
=======================================================================
GET	​/user​/{username}	Get user by user name
Parameters: username
Responses:
code: 200
Response body:
  {
    "id": 1,
    "username": "theUser",
    "firstName": "John",
    "lastName": "James",
    "email": "john@email.com",
    "password": "12345",
  }
code: 400
Response body:
  {
    "error": "User not found"
  }
=======================================================================
PUT	​/user​/{username}	Update user
Parameters: username
Request body:
{
  "username": "newtheUser",
  "firstName": "newJohn",
  "lastName": "newJames",
  "email": "john@email.com",
  "password": "12345",
}
Responses:
code: 200
Response body:
{
  "id": 1,
  "username": "newtheUser",
  "firstName": "newJohn",
  "lastName": "newJames",
  "email": "john@email.com",
  "password": "12345",
}
code: 400
Response body:
{
  "error":"not valid request data",
}
code: 404
Response body:
{
  "error":"User not found",
}
=======================================================================
DELETE	​/user​/{id}	Delete user by id
Responses:
code: 200
Response body: {}
code: 404
Response body:
{
  "error":"User not found",
}
=================================================
"""

import json
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
import re


class Users:
    def __init__(self, id: int, username: str, firstName: str, lastName: str, email: str, password: str):
        self.id = id
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password


USERS_LIST = [
    {
        "id": 1,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
    }
]

error = {"error": "User not found"}


def valid_user(data):
    print(data)
    if data.get("id") and data.get("username") and data.get("firstName") and data.get("lastName") and data.get("email") \
            and data.get("password"):
        return True
    else:
        return False


def valid_users_list(data):
    for item in data:
        if not valid_user(item):
            return False
    return True


def update_user(data: dict, new_data: dict):
    for key, value in new_data.items():
        data[key] = value
    return data


def create_user(data):
    """
    {'id': 1, 'username': 'theUser', 'firstName': 'John', 'firstName': 'James', 'email': 'john@email.com',
    'password': '12345'}
    :param data:
    :return:
    """
    unique_id = True
    if valid_user(data):
        for user in USERS_LIST:
            if user.get("id") == data.get("id"):
                unique_id = False
                break
        if unique_id:
            USERS_LIST.append(Users(**data).__dict__)
            print(USERS_LIST)
    else:
        unique_id = False
    return unique_id


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_response(self, status_code=200, body=None):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(body if body else {}).encode('utf-8'))

    def _pars_body(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        return json.loads(self.rfile.read(content_length).decode('utf-8'))  # <--- Gets the data itself

    def do_GET(self):
        logging.info("GET request,\nPath: % s\nHeaders:\n % s\n ", str(self.path), str(self.headers))
        if self.path == "/reset":
            USERS_LIST.clear()
            USERS_LIST.append({
                "id": 1,
                "username": "theUser",
                "firstName": "John",
                "lastName": "James",
                "email": "john@email.com",
                "password": "12345",
            })
            self._set_response(status_code=204)
        if self.path == "/users":
            self._set_response(status_code=200, body=USERS_LIST)
        if self.path.startswith("/user/"):
            print(self.path)
            username = self.path.lstrip("/user/")
            print(username)
            for user in USERS_LIST:
                if user.get('username') == username:
                    find_user = user
                    self._set_response(status_code=200, body=find_user)

                else:
                    self._set_response(status_code=400, body=error)
        # else:
        #     self._set_response()
        #     self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        logging.info("POST request,\nPath: % s\nHeaders:\n % s\n ", str(self.path), str(self.headers))
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        # print("****************************************\n",post_data)
        message = json.loads(post_data)
        # print("message ",message)
        if self.path == "/user":
            # print(Users(**message))
            if create_user(message):
                # print("!########################################################")
                self._set_response(status_code=201, body=message)
                # self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
            else:
                self._set_response(status_code=400)
                # self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
        if self.path == "/user/createWithList":
            if valid_users_list(message):
                for item in message:
                    create_user(item)
                self._set_response(status_code=201, body=message)
            else:
                self._set_response(status_code=400)
        # else:
        #     self._set_response()
        #     self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_PUT(self):
        logging.info("PUT request,\nPath: % s\nHeaders:\n % s\n ", str(self.path), str(self.headers))
        put_data = self._pars_body()
        #print(put_data)
        #print("**************")
        if self.path.startswith("/user/"):
            username = self.path.lstrip("/user/")
            print(username)
            print("Put data ", put_data.get("username"))

            def find_user_for_update(user_name, user_list):
                update = False
                for user in user_list:
                    if user.get('username') == user_name:
                        update = True
                return update
            result = find_user_for_update(username,USERS_LIST)
            if not result:
                self._set_response(status_code=404, body=error)
                return
            if not put_data.get("username"):
                self._set_response(status_code=400, body={"error": "not valid request data"})
                return
            if result:
                for user in USERS_LIST:
                    if user.get('username') == username:
                        user2 = update_user(user, put_data)
                        USERS_LIST.remove(user)
                        USERS_LIST.append(user2)
                        self._set_response(status_code=200, body=user2)
                        return



        # self._set_response()
        # self.wfile.write(json.dumps(put_data).encode('utf-8'))

    def do_DELETE(self):
        logging.info("DELETE request,\nPath: % s\nHeaders:\n % s\n ", str(self.path), str(self.headers))
        if self.path.startswith("/user/"):
            print(self.path)
            id = int(self.path.lstrip("/user/"))
            print(id)
            for user in USERS_LIST:
                if user.get('id') == id:
                    print(user)
                    USERS_LIST.remove(user)
                    self._set_response(status_code=200)

                else:
                    self._set_response(status_code=404, body=error)


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    logging.basicConfig(level=logging.INFO)
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
