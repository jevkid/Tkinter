from student import Student
from storage import Storage
from question import TestQuestion

class Test():

	# This class provides the functionality to:
	# - Store up to 10 test questions.
	# - Give the student points if they answer question correctly.
	# - Time how long it takes a student to answer each question.
	#    + If the question is answered quickly they may be eligible
	#      for bonus points.
	# - Display previous test statistics

	def __init__(self):
		self.questions = []
		self.indexOfCurrentQuestion = 0
		self.results = dict()
		self.timeElapsed = 0
		self.countingIsActive = False
		self.student = Student()
		self.storage = Storage()

	def updatePoints():
		# TODO
		print "test"

	def countSeconds():
		# TODO
		print "test"

	def computePoints():
		# TODO
		print "test"

	def nextQuestionExists():
		# TODO
		print "test"

	def goToNextQuestion():
		# TODO
		print "test"

	def displayTestStatistics():
		# TODO
		print "test"