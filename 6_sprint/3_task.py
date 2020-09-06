"""
In user.json file we have information about users in format
[{“id”: 1, “name”: “userName”, “department_id”: 1}, ...],

in file department.json are information about departments in format:
[{“id”: 1, “name”: “departmentName”}, ...].

Function user_with_department(csv_file, user_json, department_json) should read from
json files information and create csv file in format:

header line - user, department

next lines :  <userName>, <departmentName>

If file department.json doesn't contain department with department_id from user.json
we generate DepartmentName exception.

Create appropriate json-schemas for user and department.

If schema for user or department doesn't satisfy formats described above we should
generate InvalidInstanceError exception

To validate instances create function validate_json(data, schema)
"""
import json
import csv
import jsonschema
from jsonschema import validate


class DepartmentName(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class InvalidInstanceError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


user_schema = {
    "type": "object",
    "required": ["id", "name", "department_id"],
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "department_id": {"type": "number"}
    }
}

department_schema = {
    "type": "object",
    "required": ["id", "name"],
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
    }
}


def validate_json(data, schema):
    try:
        for i in data:
            validate(i, schema)
    except jsonschema.exceptions.ValidationError:
        return False
    return True


def csv_writer(path, header, data):

    with open(path, "w", newline='') as out_file:
        writer = csv.writer(out_file, delimiter=',')
        writer.writerow(header)
        for row in data:
            writer.writerow(row)


def user_with_department(csv_file, user_json, department_json):
    header_line = ["name", "department"]
    csv_list = []
    with open(user_json) as user_json:
        user_data = json.load(user_json)
    with open(department_json) as department_json:
        department_data = json.load(department_json)
    # validation
    if not validate_json(user_data, user_schema):
        raise InvalidInstanceError("Error in user schema")
    if not validate_json(department_data, department_schema):
        raise InvalidInstanceError("Error in department schema")

    # Check if file department.json doesn't contain department with department_id from user.json
    for item in user_data:
        flag = False
        for d in department_data:
            if item.get("department_id") == d.get("id"):
                flag = True
                csv_list.append([item["name"], d["name"]])
                break
        if not flag:
            raise DepartmentName(f"Department with id {item.get('department_id')} doesn't exists")
    # write to csv
    csv_writer(csv_file, header_line, csv_list)


try:
  user_with_department("user_department.csv", "user_without_dep.json", "department.json")
except DepartmentName as e:
    print(str(e))
#except InvalidInstanceError as ev:
#    print(str(ev))
user_with_department("user_department.csv", "user.json", "department.json")
#print_file("user_department.csv")

try:
  user_with_department("user_department.csv", "user_without_dep_id.json", "department.json")
except InvalidInstanceError as e:
    print(str(e))