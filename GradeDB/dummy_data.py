# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 19:22:59 2022

@author: hp
"""
from schema import Student, engine
from sqlalchemy.orm import sessionmaker
from gradedb import Grade


db = Grade("gradeDB") 

students =[{"username": "Okey", 'email':"Okey@company.com"},
        {"username": "Bila", 'email':"Bila@alchemy.nl"},
        {"username": "Selin", 'email':"selin@yahoo.com"},
        {"username": "Guraw", 'email':"guraw@hotmail.com"},
        {"username": "Baluwa", 'email':"balwal@gmail.com"}
        ]

for s in students:
    db.addStudent(student_name=s['username'], student_email=s['email'])
total_students=db.allQuestions()

for s in total_students:
    print(s.name)

print(total_students)

