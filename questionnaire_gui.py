from classes.student import Student
from classes.storage import Storage
from classes.question import Question

class Questionnaire():

	# This class acts as a container for up to 10 questions and provides an
	# interface through which the user will be able to view a question and
	# select an answer.

	def __init__(self):
		self.questions = []
		self.aptitudeChart = None # TODO matplotlib pichart
		self.student = Student()
		self.aptitudes = self.student.getAptitudes()
		self.storage = Storage("csv/questions/questionnaire.csv")
		self.__loadQuestionData()

	# Load question data from CSV file
	def __loadQuestionData(self):
		storage = self.storage
		columns = storage.getColumns()
		columnCount = len(columns)
		rows = storage.getRows()
		data = []
		for row in rows:
			# Create a dictionary where key is column name and value is 
			# cell data. This will be added as a single element to the data 
			# list.
			rowData = dict()
			for i in range(columnCount):
				try:
					column = columns[i]
					r = row[i]
					rowData[column] = r 
				except IndexError:
					break
			data.append(rowData)

		# Instantiate question objects
		questions = self.questions
		for d in data:
			question_id = d['id'] # Value of id for this row
			question = d['question'] # Value of question for this row
			answers = []
			keys = tuple(d.iterkeys()) # These are the column names

			# Populate answers and aptitudes lists with values from CSV that 
			# have a value i.e. not blank
			answers = [d[k] for k in keys if 'answer' in k and len(d[k]) > 0]
			aptitudes = [d[k] for k in keys if 'aptitude' in k and len(d[k]) > 0]

			# Create a dictionary where key is answer and value is a  
			# another dictionary where each key is the course name and each
			# value is the number of aptitude points
			answersDictionary = dict()
			for index, answer in enumerate(answers):
				aptitude = aptitudes[index].split(';')
				apts = dict()
				for a in aptitude:
					temp = a.split()
					name = temp[0]
					points = int(temp[1])
					apts[name] = points
				aptitude = apts
				answersDictionary[answer] = aptitude 

			questionObj = Question(question)
			questionObj.setAnswers(answersDictionary)
			questionObj.setId(question_id)
			questions.append(questionObj)

		# for question in questions:
		# 	print question.getQuestion()
		# 	print question.getAnswers()

	# For this question (specified using questionIndex),
	# update the student's aptitude points for the answer
	# they have provided.
	# @param answer  the answer string
	# @param questionIndex  the index of the question
	def updateStudentAptitude(self, questionIndex, answer):
		question = self.questions[questionIndex]
		answers = question.getAnswersDictionary()
		try:
			aptitudes = question.getAnswersDictionary()[answer]
			for name, points in aptitudes.iteritems():
				aptitude = self.student.getCourseAptitude(name)
				if aptitude != None:
					aptitude.updateAptitude(points)
			return ""
		except KeyError:
			print "KeyError: Invalid answer!"

	def calculateSuggestedCourse(self):
		aptitudes = self.student.getAptitudes()
		suggestedCourse = aptitudes[0]
		for aptitude in self.student.getAptitudes():
			if aptitude.getPoints() > suggestedCourse.getPoints():
				suggestedCourse = aptitude
		if suggestedCourse.getName() == 'cs':
			csWiths = [c for c in aptitudes if '_' in c.getName()]
			suggested = csWiths[0]
			for csWith in csWiths:
				if csWith.getPoints() > suggested.getPoints():
					suggested = csWith
			if suggested.getPoints() > 0:
				return suggested
		return suggestedCourse

q = Questionnaire()
import random

for index, question in enumerate(q.questions):
	print index+1, question.getQuestion()
	answers = question.getAnswersDictionary().keys()
	r = random.randint(0,len(answers)-1)
	answer = answers[r]
	print answer + '\n'
	q.updateStudentAptitude(index, answer)

aptitudes = q.student.getAptitudes()
for aptitude in aptitudes:
	name = aptitude.getName()
	points = aptitude.getPoints()
	print name, points

course = q.calculateSuggestedCourse()
print "Suggested Course: %s" %course.getName()