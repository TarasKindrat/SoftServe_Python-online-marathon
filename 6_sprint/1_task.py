"""
Create function find(file, key)

This function parses json-file and returns all unique values of the key.
1.json:
[{"name": "user_1”, "password": "pass_1”},
{"name": "user_2”, "password": ["pass_1", "qwerty“]} ]

find("1.json", "password") returns ["pass_1", "qwerty"]
2.json:
[{"name": "user_1”, "credentials": {"username": "user_user”, "password": "1234qweQWE"}}, {"name": "user_2”, "password": ["pass_1 ", "qwerty "]}]

find("2.json", "password") returns ["1234qweQWE", "pass_1", "qwerty"]
3.json:
{"name": "user_1","credentials": {"username": "user_user","password": "1234qweQWE"}}

find("3.json", "password") returns ["1234qweQWE"]
"""


def find(file, key):
    import json
    list_keys = []
    with open(file) as file:
        json_data = json.load(file)
    if isinstance(json_data, list):
        for x in json_data:
            for key_d, value in x.items():
                if isinstance(value, dict):
                    json_data.append(value)
                if key_d == key:
                    if isinstance(value, list) and value not in list_keys:
                        for j in value:
                            if j in list_keys:
                                list_keys.remove(j)
                        list_keys.extend(value)
                    if value not in list_keys and not isinstance(value, list):
                        list_keys.append(value)
    if isinstance(json_data, dict):
        for key_d, value in json_data.items():
            if isinstance(value, dict):
                json_data[key] = value
            if key_d == key:
                if isinstance(value, list) and value not in list_keys:
                    for j in value:
                        if j in list_keys:
                            list_keys.remove(j)
                    list_keys.extend(value)
                if value not in list_keys and not isinstance(value, list):
                    list_keys.append(value)
    return list_keys


print(find("1.json", "password"))
print(find("2.json", "password"))
print(find("3.json", "password"))
print(find("4.json", "password"))
