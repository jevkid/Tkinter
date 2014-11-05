from Tkinter import *
import tkMessageBox
from Response import Response
from DisplayResults import *

class Questionnaire(Frame):
    # GUI Setup
	def __init__(self, master):
  	# Initialise Questionnaire Class
        
		Frame.__init__(self, master) 
  		self.grid()
		self.createTeamExpQuest()
		self.createButtons()
		self.clearResponse()
		self.storeResponse
		self.openResultsWindow()
	def createTeamExpQuest(self):
		#Create widgets to ask Team Experience Questions
		#Question 1
		lblStrAgr = Label(self, text= 'Aptitude Program:', font =('MS', 14, 'bold'))
		lblStrAgr.grid(row = 1, column = 0, rowspan = 2)
		#When faced with a difficult problem and you are unsure of the best way to solve it you:
		lblStrAgr = Label(self, text= '1. When faced with a difficult problem and you are unsure of the best way to solve it you:', font =('MS', 7))
		lblStrAgr.grid(row = 6, column = 0, rowspan = 2)
		#Get started on solving it right away and apply trial and error (0p)
		lblStrAgr = Label(self, text= 'a.)  Get started on solving it right away and apply trial and error (0p)', font =('MS', 7))
		lblStrAgr.grid(row = 8, column = 1, rowspan = 1)
		#Communicate with experienced people and solve it as a team effort (BIS 4p, CS 2p and SE 3p)
		lblStrAgr = Label(self, text= 'b.) Communicate with experienced people and solve it as a team effort (BIS 4p, CS 2p and SE 3p)', font =('MS', 7))
		lblStrAgr.grid(row = 10, column = 1, rowspan = 2)
		#Split the problem into smaller, easier to manage chunks and focus on solving each of these smaller problems (BIS 2p, SE 4p, CS 3p)
		lblStrAgr = Label(self, text= 'c.) Split the problem into smaller, easier to manage chunks and focus on solving each of these smaller problems (BIS 2p, SE 4p, CS 3p)', font =('MS', 7))
		lblStrAgr.grid(row = 12, column = 1, rowspan = 2)
		#Radio Button
		#Question 1
		self.varQ1 = IntVar()

		R1Q1 = Radiobutton (self, variable = self.varQ1, value = 4)
		R1Q1.grid (row = 8, column = 0)

		R2Q1 = Radiobutton (self, variable = self.varQ1, value = 3)
		R2Q1.grid (row = 10, column = 0) 

		R3Q1 = Radiobutton (self, variable = self.varQ1, value = 2)
		R3Q1.grid(row = 12, column = 0)
		
		#Question 2
#Question 1
		#Suppose you are involved in developing a software application. Select the statement that appeals most to you:
		lblStrAgr = Label(self, text= '2. Suppose you are involved in developing a software application. Select the statement that appeals most to you:', font =('MS', 7))
		lblStrAgr.grid(row = 16, column = 0, rowspan = 2)
		# I would be developing the application where I would take working existing solutions from other applications, put them together and implement them into the software application (SE 5, BIS 2, CS 3)
		lblStrAgr = Label(self, text= 'a.)   I would be developing the application where I would take working existing solutions from other applications, put them together and implement them into the software application (SE 5, BIS 2, CS 3)', font =('MS', 7))
		lblStrAgr.grid(row = 18, column = 1, rowspan = 1)
		#I would be researching and applying computer science and mathematical concepts to make sure the system operates as fast and efficient as it can (CS 5)
		lblStrAgr = Label(self, text= 'b.) I would be researching and applying computer science and mathematical concepts to make sure the system operates as fast and efficient as it can (CS 5)', font =('MS', 7))
		lblStrAgr.grid(row = 20, column = 1, rowspan = 2)
		# I would be in constant communication with both the software developers and the client to ensure the software is being designed to meet their exact requirements.  (BIS 5)
		lblStrAgr = Label(self, text= 'c.)  I would be in constant communication with both the software developers and the client to ensure the software is being designed to meet their exact requirements.  (BIS 5)', font =('MS', 7))
		lblStrAgr.grid(row = 22, column = 1, rowspan = 2)
		#Radio Button
		#Question 1
		self.varQ2 = IntVar()

		R1Q2 = Radiobutton (self, variable = self.varQ2, value = 4)
		R1Q2.grid (row = 18, column = 0)

		R2Q2 = Radiobutton (self, variable = self.varQ2, value = 3)
		R2Q2.grid (row = 20, column = 0) 

		R3Q2 = Radiobutton (self, variable = self.varQ2, value = 2)
		R3Q2.grid(row = 22, column = 0)
		
	#def createComments(self):
		#Sets up comments and name entries
		#Name
		lblComm = Label (self, text = 'Name (optional):', font = ('MS', 8, 'bold'))
		lblComm.grid(row = 1, column = 1, rowspan = 2)

		self.entName = Entry(self)
		self.entName.grid(row = 1, column = 2, columnspan = 2, sticky = E)

	def createButtons(self):
		#Creates the buttons
		butSubmit = Button (self, text = 'Submit', font = ('MS', 8, 'bold'))
		butSubmit['command'] = self.storeResponse #Note: no () after the method
		butSubmit.grid(row = 24, column = 3, columnspan = 2)

		#Creates the buttons
		butSubmit = Button (self, text = 'Clear', font = ('MS', 8, 'bold'))
		butSubmit['command'] = self.clearResponse #Note: no () after the method
		butSubmit.grid(row = 24, column = 5, columnspan = 2)

		butSubmit = Button (self, text = 'View Results', font = ('MS', 8, 'bold'))
		butSubmit['command'] = self.openResultsWindow #Note: no () after the method
		butSubmit.grid(row = 24, column = 7, columnspan = 2)

	def clearResponse(self):
		self.varQ1.set(0)
		self.varQ2.set(0)
		#add other buttons

		#self.entName.delete(0, END)
		#self.txtComment.delete(0, END)
	def storeResponse(self):
		#Store the results of the Questionnaire
		index = self.listProg.curselection()[0]
		strProg = str(self.listProg.get(index))
		strMsg = ""

		if strProg == "":
			strMsg = "You need to select a Degree Programme "

		if (self.varQ1.get() == 0) or (self.varQ2.get() == 0) or (self.varQ3.get() == 0):
			strMsg = strMsg + "You need to answer all Team Experience Questions"
		else:
			tkMessageBox.showwarning("Entry Error", strMsg)
		
		if strMsg == "":

			import shelve
			db = shelve.open('responsedb')
			responseCount = len(db)
			Ans = Response (str(responseCount+1), strProg,
							self.varQ1.get(), self.varQ2.get(), self.varQ3.get())
			db[Ans.respNo] = Ans
			db.close
		
			tkMessageBox.showinfo("Questionnaire", "Questionnaire Submitted")
			self.clearResponse()
		else: 
 			tkMessageBox.showwarning("Entry Error", strMsg)

	def openResultsWindow(self):

		t1 = Toplevel(root)
		DisplayResults(t1)


#Main
root = Tk()
root.title("Teamwork Questionnaire")
app = Questionnaire(root)
root.mainloop()