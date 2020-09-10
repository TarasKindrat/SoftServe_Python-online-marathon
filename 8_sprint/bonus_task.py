"""
Припустимо. що ми розробляємо додаток, який буде зберігати та відображати оцінки студентів за певними предметами.
Для того щоб працювати з додатком, ми маємо зробити три кроки

 1. Початок - з файлів зчитуємо інформацію про предмети, студентів та оцінки  втакому форматі
users = [{"username": "Trainee1", "id": 1, "role": 0, "password": "b'$2b$12$Y6yYP3cnzbKeIY7TfSmTIu9v/kGkdVmD/1zvMzU4iGhjAg6k8hHgu'"}]
subjects = [{"title": "Mathematics", "id": 1}, {"id":2, "title": "Software Design"}]
grades = [{"user_id":1, "subject_id": 2, "score": "B"},
          {"user_id":1, "subject_id": 1, "score": "C"}]
 та створюємо відповідні лісти класів users та subjects.
2. Імітуємо роботу з додатком
створюємо юзерів,
додаємо створених юзерів до users (у випадку унікальності username)
створюємо нові предмети,
додаємо створені предмети до subjects (у випадку унікальності title),
додаємо оцінки по певному предмету для юзера,
показуємо всі оцінки студента (або студенту тільки свої оцінки або ментору)
3.Переписуємо старі json-файли новими


Можлива послідовність кроків
users = []
subjects = []

# start : read all from json-files

# get_subjects_from_json("json_file") -> subjects
# create users with grades
# get_users_with_grades("user.json", "subject.json", "grades.json") -> users


user = User.create_user("username", "password")
# -> check password (min 6 symbols, UpperCase, LowerCase, Number, Non AlphaNumerical Symbols) and
# -> create user with hashed password (brypt) and uuid (uuid4()) as id) if all is OK otherwise raise exception
# ->


user = User.create_user("username", "passworD7?")
authorized_user = User.create_user("mentor", "Password!1", Role.Mentor)

user.add_score_for_subject(subjects[0], Score.A)

add_user(user, users)  # -> check is username is unique and adds user to users

check_if_user_present("username", "password", users) # -> return true or Exception if user with username and password doesn't exists in users

get_grades_for_user(user, authorized_user, users) #-> return grades for user (if authorized_user is mentor or authorized_user == user)

#end : write all to json-files (users##.json, subjects##.json, grades##.json) with date-based name

***************************************************************************************************
1. Create users and subjects data from files

get_subjects_from_json(subjects_json)

get_users_with_grades(users_json, subjects_json, grades_json)

2. Simulate working with the application

method User.create_user(username, password, role) creates user

method user.add_score_for_subject(subject:Subject, score: Score) adds score for subject

function add_user(user, users) adds user to users (in case of uniqueness username)

function add_subject(subject, subjects) adds subject to subjects (in case of uniqueness title)

function get_grades_for_user(username:str, user:User, users:list) returns all grades for the user with username (only own grades or for mentor)

3. Rewrite the old json-files with new ones

users_to_json(users, json_file)

subjects_to_json(subjects, json_file)

grades_to_json(users, subjects, json_file)
"""

import json
from enum import Enum
users = []
subjects = []


class FileType(Enum):
    JSON = "JSON"
    BYTE = "BYTE"


class Role(Enum):
    Trainee = "Trainee"
    Mentor = "Mentor"


class Score(Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'


class NonUniqueException(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

class User:
    def __init__(self, id, username, password, role=Role.Trainee):
        self.id = id
        self.username = username
        self.password = password
        self.role = role
        self.scores = []

    def __str__(self):
        return f"{self.username } with role {self.role}: {self.scores}"

    def add_score_for_subject(self, subject, score):
        pass

    @staticmethod
    def create_user(username, password, role):
        return User(0, username, password, role)


class Subject:

    def __init__(self, id, title):
        self.id = id
        self.title = title

class Grade:
    def __init__(self, user_id, subject_id, score):
        self.user_id = user_id
        self.subject_id = subject_id
        self.score = score

def get_subjects_from_json(subjects_json):
    with open(subjects_json) as file:
        # subjects = [{"title": "Mathematics", "id": 1}, {"id":2, "title": "Software Design"}]
        data = json.load(file)
    for item in data:
        for i in subjects:
            if i.get("title") == item.get("title"):
                break
        subjects.append(Subject(item.get("id"), item.get("title")))
    return subjects

def get_grades_fron_json(grades_json):
    with open(grades_json) as grades:
        grades_data = json.load(grades)
    for item in grades_data:
        grades.append(Grade(item.get("user_id"),item.get("subject_id"),item.get("score")))
    return grades

def get_users_with_grades(users_json, subjects_json, grades_json):
    # users = [{"username": "Trainee1", "id": 1, "role": 0,
    #           "password": "b'$2b$12$Y6yYP3cnzbKeIY7TfSmTIu9v/kGkdVmD/1zvMzU4iGhjAg6k8hHgu'"}]
    # subjects = [{"title": "Mathematics", "id": 1}, {"id": 2, "title": "Software Design"}]
    # grades = [{"user_id": 1, "subject_id": 2, "score": "B"},
    #           {"user_id": 1, "user_id": 1, "score": "C"}]

    subjects = get_subjects_from_json(subjects_json)

    grades = get_grades_fron_json(grades_json)

    with open(users_json) as user:
        users_data = json.load(user)
    for item in users_data:
        users.append(User(item.get('id'), item.get('username'), item.get("password"), item.get("role")))

    for user in users:
        for subject in subjects:
            for grade in grades:
                if user.id == subject.id == grade.user_id:
                    user.scores.append({subject.title: grade.score})
    return users


# adds user to users (in case of uniqueness username)
def add_user(user, users):
    for item in users:
        if item.username == user.username:
            Flag = False
            raise NonUniqueException(f"User with name {user.username} already exists")
            break
    users.append(user)

# adds subject to subjects (in case of uniqueness title)
def add_subject(subject, subjects):
    pass

# returns all grades for the user with username (only own grades or for mentor)
def get_grades_for_user(username:str, user:User, users:list):
    #print(get_grades_for_user("Trainee1", users[1], users))
    pass

# Rewrite the old json-files with new ones
def users_to_json(users, json_file):
    pass

def subjects_to_json(subjects, json_file):
    pass

def grades_to_json(users, subjects, json_file):
    pass

def check_password():
    pass


def check_if_user_present(name, password, users_list):
    for item in users_list:
        if item.username == name and item.password == password:
            return True
    return False


"""
users = get_users_with_grades("users.json", "subjects.json", "grades.json")
print(len(users))

	

1

	

1

	
	

subjects = get_subjects_from_json("subjects.json")
print(len(subjects))

	

2

	

2

	
	

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
print(mentor)

	

Mentor with role Role.Mentor: []

	

Mentor with role Role.Mentor: []

	
	

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
student = User.create_user("Mentor", "!1qQ456", Role.Trainee)
try:
  add_user(student, users)
except NonUniqueException as e:
  print(str(e))

	

User with name Mentor already exists

	

User with name Mentor already exists

	
	

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
print(check_if_user_present("Mentor", "aaaaaa", users))
print(check_if_user_present("Mentor", "!1qQ456", users))

	

False
True

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
print(get_grades_for_user("Trainee1", users[1], users))

	

[{'Software Design': 'B'}, {'Mathematics': 'C'}]

	

None

	
	

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
print(get_grades_for_user("Mentor", users[1], users))

	

[]

	

None

	
	

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
subjects = get_subjects_from_json("subjects.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 =  User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
print(len(users))
print(user2)

	

3
Second with role Role.Trainee: [{'Software Design': 'B'}]

	

3
Second with role Role.Trainee: []

	
	

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
subjects = get_subjects_from_json("subjects.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 =  User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
subject = Subject("New Subject")
add_subject(subject, subjects)
users[0].add_score_for_subject(subject, Score.D)

print(get_grades_for_user("Trainee1", users[1], users))

	

[{'Software Design': 'B'}, {'Mathematics': 'C'}, {'New Subject': 'D'}]

	

***Error***
Traceback (most recent call last):
  File "__tester__.python3", line 276, in <module>
    subject = Subject("New Subject")
TypeError: __init__() missing 1 required positional ar
"""