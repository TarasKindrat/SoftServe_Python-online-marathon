"""
Class Student has attributes full_name:str, avg_rank: float, courses: list

Class Group has attributes title: str, students: list.

Json-files represent information about student (students).

Create methods:

Student.from_json(json_file) that return Student instance from attributes from json-file;

Group.serialize_to_json(list_of_groups, filename)

Group.create_group_from_file(students_file)

Parse given files, create instances of Student class and create instances of Group class
 (title for group is name of json-file without extension).
"""
import json


class Student:
    def __init__(self, full_name: str, avg_rank: float, courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

    @classmethod
    def from_json(cls, json_file):
        with open(json_file) as file:
            data = json.load(file)
        return cls(**data)


class Group:
    def __init__(self, title: str, students: list):
        self. title = title
        self.students = students

    def __str__(self):
        return f"{self.title}: {[str(student) for student in self.students]}"

    @classmethod
    def create_group_from_file(cls, students_file):
        group = []
        with open(students_file) as file:
            data2 = json.load(file)
        if isinstance(data2, list):
            for d in data2:
                group.append(Student(**d))
        if isinstance(data2, dict):
            group.append(Student(**data2))
        return cls(str(students_file).split('.')[0], group)

    def serialize_to_json(list_of_groups, filename):
        dump_list = []

        def cond(val, group_s):
            if not isinstance(val, list):
                result = val
            if isinstance(val, list):
                val_list = [student.__dict__ for student in group_s.students]
                result = val_list
            return result

        for group in list_of_groups:
            dump_list.append({key: cond(value, group) for (key, value) in group.__dict__.items()})
        with open(filename,"w") as file:
            json.dump(dump_list, file)

"""
[{"title": "2020_2", "students": [{"full_name": "Student 1 from second Group", "avg_rank": 98, "courses": 
["Python"]}, {"full_name": "Student 2 from second Group", "avg_rank": 70.34, "courses": 
["Ruby", "Python", "Frontend development"]}]}, {"title": "2020-01", "students": 
[{"full_name": "Student2 from group2", "avg_rank": 50.4, "courses": ["C++"]}]}]"""
user1 = Student.from_json("2020-01.json")
print(user1)

# with open("2020_2.json") as read_file:
#     user2 = json.load(read_file)
# print([str(Student(**item)) for item in user2])

g1 = Group.create_group_from_file("2020_2.json")
g2 = Group.create_group_from_file("2020-01.json")
Group.serialize_to_json([g1, g2], "g1")
#for i in g2.students:
#    print(i)
print(g1)
#print(g1.title)
#print(g2.title)