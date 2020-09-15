import json
from http.server import HTTPServer, BaseHTTPRequestHandler

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


class Users:
    def __init__(self, id: int, username: str, firstName: str, lastName: str, email: str, password: str):
        self.id = id
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password


error = {"error": "User not found"}


def valid_user(data):

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

def chek_user_id(data):
    unique_id = True
    if valid_user(data):
        for user in USERS_LIST:
            if user.get("id") == data.get("id"):
                unique_id = False
                break
    else:
        unique_id = False
    return unique_id


def create_user_add_to_list(data):
    if chek_user_id(data):
        USERS_LIST.append(Users(**data).__dict__)
        return True
    else:
        return False


def check_id_users_from_list(data_list):
    flag = True
    for data in data_list:
        for user in USERS_LIST:
            if data.get("id") == user.get("id"):
                flag = False
                break
    return flag


def find_user_for_update(user_name, user_list):
    update = False
    for user in user_list:
        if user.get('username') == user_name:
            update = True
    return update

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


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself

        message = json.loads(post_data)

        if self.path == "/user":

            if create_user_add_to_list(message):

                self._set_response(status_code=201, body=message)

            else:
                self._set_response(status_code=400)

        if self.path == "/user/createWithList":
            if valid_users_list(message) and check_id_users_from_list(message):
                for item in message:
                    create_user_add_to_list(item)
                self._set_response(status_code=201, body=message)
            else:
                self._set_response(status_code=400)

    def do_PUT(self):
        put_data = self._pars_body()

        if self.path.startswith("/user/"):
            username = self.path.lstrip("/user/")

            result = find_user_for_update(username, USERS_LIST)
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


    def do_DELETE(self):
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


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, host='localhost', port=8000):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
