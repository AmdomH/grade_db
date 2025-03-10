# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 11:44:05 2022

@author: hp
"""

from schema import Student, engine, Assignment, Questions, TaskQ, Submission, Answers, Base
from schema import EvaluationRequest, Evaluation
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, delete
from datetime import datetime

Base.metadata.create_all(engine)

class Grade:
  def __init__(self, fileName):
    addr = "sqlite:///" + fileName
    self._engine = create_engine(addr,echo=True)
    self._sessionMaker = sessionmaker(bind=engine)
  def newSession(self):
    return self._sessionMaker()

  def addStudent(self, student_name, student_email):
      with self.newSession() as session:
            student=Student(name=student_name, email=student_email)
            session.add(student)
            session.commit()
            return student.university_id
  def allStudents(self): 
      with self.newSession() as ses: 
          return ses.query(Student).all()
  def addQuestion(self, title, text ):
      with self.newSession() as ses:
          ques=Questions( title=title, content=text)
          ses.add(ques)
          ses.commit()
          return ques.title
     
  def allQuestions(self): 
      with self.newSession() as ses: 
          return ses.query(Questions).all()
      
  def addTask(self, task_id, title, overview) :
      with self.newSession() as ses:
          ques_ID=int(input("Add question ID:- "))
          question=ses.query(Questions).filter(Questions.question_id== ques_ID).one()
          task=TaskQ(task_id=task_id, task_title=title, task_Overview=overview)
          task.questions=question
          ses.add(task)
          ses.commit()
  def allTask(self):
      with self.newSession() as ses:
          return ses.query(TaskQ).all()
  def addAssignment(self, date):
      with self.newSession() as ses:
          student_ID=int(input("Add student ID:- "))
          task_ID=int(input("Add task ID here: "))
          universityID=ses.query(Student).filter(Student.university_id== student_ID).one()
          taskID=ses.query(TaskQ).filter(TaskQ.task_id== task_ID).one()
          
          assignment=Assignment(assignment_deadline=date)
          assignment.students = universityID
          assignment.tasks = taskID
          ses.add(assignment)
          ses.commit()
          print("New Assignment has been added by the teacher ", assignment.assignment_id)
 

  def new_submission(self):
      with self.newSession() as ses:
          assignment_ID=int(input("Add the assignment ID: "))
          assignmentID=ses.query(Assignment).filter(Assignment.assignment_id == assignment_ID)
          subm= Submission()
          subm.assignments = assignmentID 
          ses.add(subm)
          ses.commit()
        
  def add_answer(self, answer):
      with self.newSession() as ses:
          ques_ID=int(input("Add question ID:- "))
          question=ses.query(Questions).filter(Questions.question_id== ques_ID).one()
          subm_ID = int(input("Enter submissionID:"))
          submission=ses.query(Submission).filter(Submission.submission_id==subm_ID).one()
          
          answer=Answers(answer_text=answer)
          answer.questions=question
          answer.submissions=submission
          ses.add(answer)
          ses.commit()
          
  def commitSubmission(self):
      with self.newSession() as ses:
          subm_ID = int(input("Enter your submission ID: "))
          submission=ses.query(Submission).filter(Submission.submission_id==subm_ID).one()
          print("This is submission has been commited:", submission)
          evaluation_request=EvaluationRequest()
          
          evaluation_request.submission_id=submission 
          ses.add(evaluation_request)
          ses.commit()
          
  def add_newEvaluation(self):
      with self.newSession() as ses:
          eva_request_ID=int(input("Enter Eva request ID here: "))
          evalu=ses.query(EvaluationRequest).filter(EvaluationRequest.evaluation_request_id==eva_request_ID).one()
          
          evaluation=Evaluation()
          evaluation.evaluation_request=evalu
          ses.add(evaluation)
          ses.commit()
  def add_score(self):
      with self.newSession() as ses: 
          eva_ID = int(input("Enter the evaluation ID: "))
          evaluation=ses.query()

