import requests
import json
"""
In case  we need to get information about different entities in the json-format that are
 returned as a result of a request to the server.
Create a get_request(url) function returns a lambda function that receives url parameters as
keyword arguments.
This lambda function should return json object.
"""


def get_request(url):
    response = ((requests.get(url)).json())
    # return lambda **data: [item for item in response if data == (dict(item.items() & data.items()))]
    return lambda **data: [item for item in response if data == {x: item[x] for x in item if x in data}]

comments = get_request("https://jsonplaceholder.typicode.com/comments")

print(comments(postId=1, email='Lew@alysha.tv'))
print(len(comments(postId=1)))
users = get_request("https://jsonplaceholder.typicode.com/users")
print(users(name="Leanne Graham"))

