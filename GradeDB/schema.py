# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 11:40:14 2022

@author: hp
"""

''' This module includes imported sqlalchemy library, used to define the schema and tables for grade
system databases. tables are created based ER daigram designed by group 13. under the class definitions
there is sample code for testing the functionality of the system. there is no special requirement to run
this .py module. in the next module called "gradedb" are all the access and query methods which are useful
to interact with the databse. there is also a module named, "dummy_data" which is used to populate the database
'''
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy import ForeignKey, MetaData, inspect, delete, text
from datetime import datetime
import os


print(os.getcwd())

db_url ="sqlite:/// "+ "gradeDB.db" # we are crearting our DB in sqlite and name it GradeDB

engine = create_engine(db_url, echo=True)

Base = declarative_base()

class Student(Base):
    
    """This table class represents student rows in  the table Student of the
        the gradeDB, and it has three attributes"""
        
    __tablename__='students'
    university_id=Column(Integer(), primary_key=True)
    name=Column(String, nullable=False, unique=False)
    email=Column(String, unique=True, nullable=False)
    assignment=relationship("Assignment", backref="students")

    def __repr__(self):
        return f"STUDENT:<Student_ID: {self.university_id}, Email: {self.email}>"

class Questions(Base):
    
    """ this is a table of questions with that will be assigned to taks later"""
    
    __tablename__='questions'
    question_id = Column(Integer(), primary_key=True)
    title=Column(String(), nullable=False)
    content=Column(String())   #text is known word, so changed it
    task=relationship("TaskQ", backref='questions')
    answer = relationship("Answers", backref='questions')
    
    
    def __repr__(self):
        return f"<Question ID:{self.question_id}, Title: {self.title}"
 
class TaskQ(Base):
    """ Doc str  """
    __tablename__='tasks'
    
    taskq_id = Column(Integer(), primary_key=True)
    task_id=Column(Integer, nullable=False, unique=False)
    task_title=Column(String, nullable=False)
    question_id=Column(Integer, ForeignKey('questions.question_id'), unique=True)
    task_Overview=Column(String, nullable=False)
    assign = relationship("Assignment", backref='tasks')
    
    def __repr__(self):
        return f"TASK<< Task ID:{self.task_id}, Task title:{self.task_title}, Question ID:{self.question_id}>>"


class Assignment(Base):
    """ Doc str  """
    
    __tablename__='assignments'
    assignment_id=Column(Integer, primary_key=True) 
    university_id=Column(Integer, ForeignKey('students.university_id'))
    taskq_id =Column(Integer, ForeignKey("tasks.taskq_id"))
    assignment_deadline =Column(DateTime, nullable=False)
    submission = relationship("Submission", backref='assignments')
    

class Submission(Base):
    """ Doc str  """
    
    __tablename__= 'submissions'
    submission_id=Column(Integer, primary_key=True)
    assignment_id=Column(Integer, ForeignKey('assignments.assignment_id'))
    answer = relationship("Answers", backref='submissions')
    evaluation_request= relationship("EvaluationRequest", backref='submissions')

class Answers(Base):
    """ Doc str  """
    
    __tablename__='answers'
    answer_id = Column(Integer, primary_key=True, unique=True)
    submission_id = Column(Integer, ForeignKey('submissions.submission_id'))
    question_id =Column(Integer, ForeignKey('questions.question_id'))
    answer_text = Column(String)  #can this be empty or not??
    date = Column(DateTime, default=datetime.utcnow)
    score =relationship('Score', backref='answers')


class EvaluationRequest(Base):
    """ Doc str  """
    
    __tablename__='evaluation_request'
    evaluation_request_id = Column(Integer, primary_key=True)
    submission_id=Column(Integer, ForeignKey("submissions.submission_id"))
    evalu = relationship("Evaluation", backref='evaluation_request')

    
class Evaluation(Base): 
    """ Doc str  """
    
    __tablename__='evaluation'
    evaluation_id=Column(Integer, primary_key=True, unique=True)
    evaluation_request_id=Column(Integer, ForeignKey('evaluation_request.evaluation_request_id'))
    score=relationship('Score', backref='evaluation')
    final_eval = relationship("FinalEvaluation", backref='evaluation')
    
class Score(Base):
    """ Doc str  """
    
    __tablename__= "scores"
    answer_id =Column(Integer, ForeignKey('answers.answer_id'), primary_key=True)
    evaluation_id =Column(Integer, ForeignKey('evaluation.evaluation_id'))
    Value = Column(Integer, nullable=False)

class FinalEvaluation(Base):
    """ Doc str  """
    __tablename__='final_evaluation'
    final_eval_id = Column(Integer, primary_key=True)
    evaluation_id = Column(Integer, ForeignKey('evaluation.evaluation_id'))
    
    
Base.metadata.drop_all(engine)

Base.metadata.create_all(engine)

