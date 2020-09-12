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
from http.server import HTTPServer, BaseHTTPRequestHandle

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
        else:

            self._set_response()
            self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        logging.info("POST request,\nPath: % s\nHeaders:\n % s\n ", str(self.path), str(self.headers))
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

    def do_PUT(self):
        logging.info("PUT request,\nPath: % s\nHeaders:\n % s\n ", str(self.path), str(self.headers))
        put_data = self._pars_body()
        self._set_response()
        self.wfile.write(json.dumps(put_data).encode('utf-8'))

    def do_DELETE(self):
        logging.info("DELETE request,\nPath: % s\nHeaders:\n % s\n ", str(self.path), str(self.headers))


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