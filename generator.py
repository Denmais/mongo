from pymongo import MongoClient
import random as rd
from faker import Faker

client = MongoClient(host="localhost", port= 27017, username='user', password='user')
db = client['university']


# Данные
names = ['Иван', 'Денис', 'Петр', 'Влад', 'Алиса']
surnames = ['Иванов', 'Петров', 'Бальзак', 'Мороу', 'Павлов']
groups_names = ['A1', 'B2', 'A2', 'B1', 'DD1']
departments = ['Биология', 'Информатика', 'Литература', 'Математика', 'Механика']
courses_names = ['Базы данных', 'Онтология', 'Машинное обучение', 'Алгоритмы', 'Хадуп']
fake = Faker()


# Коллекции
students = db['students']
courses = db['courses']
teachers = db['teachers']
grades = db['grades']
groups = db['groups']


new_groups = [{
    "name": rd.choice(groups_names),
} for _ in range(10)]

ngs = groups.insert_many(new_groups)
groups_id = ngs.inserted_ids

print(groups_id)

new_students= [{
    "name": rd.choice(names),
    "surname": rd.choice(surnames),
    "group": rd.choice(groups_id),
    "year_of_admission": rd.randint(2020, 2050)
} for _ in range(10)]

sp = students.insert_many(new_students)
students_id = sp.inserted_ids

new_teachers = [{
    "name": rd.choice(names),
    "surname": rd.choice(surnames),
    "department": rd.choice(departments)
} for _ in range(10)]


ts = teachers.insert_many(new_teachers)
teachers_id = ts.inserted_ids

new_courses = [{
    "course_name": rd.choice(courses_names),
    "credits": rd.randint(1,3),
    "teacher_id": rd.choice(teachers_id)
} for _ in range(10)]

cs = courses.insert_many(new_courses)
courses_id = cs.inserted_ids

new_grades = [{
    "student_id": rd.choice(students_id),
    "course_id": rd.choice(courses_id),
    "grade": rd.randint(3,5),
    "date": fake.date_time_this_year().isoformat()
} for _ in range(10)]
gs = grades.insert_many(new_grades)