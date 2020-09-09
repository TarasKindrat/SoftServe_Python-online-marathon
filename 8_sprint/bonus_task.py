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
"""