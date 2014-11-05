from Tkinter import *
import tkMessageBox
from PResponse import PResponse
from PDisplayResults import *

class Questionnaire(Frame):
    # GUI Setup
	def __init__(self, master):
  	# Initialise Questionnaire Class
        
		Frame.__init__(self, master) 
  		self.grid()
		self.createProgSelect()
		self.createTeamExpQuest()
		self.createProblems()
		self.createComments()
		self.createButtons()
		self.clearResponse()
		self.storeResponse
		self.openResultsWindow()

	def createProgSelect(self):
		#Create widgets to select a degree programme from a list

		lblProg = Label(self, text='Degree Programme:', font = ('MS', 8, 'bold'))
		lblProg.grid(row = 0, column = 0, columnspan = 2, sticky = NE)

		self.listProg = Listbox (self, height = 3)
		scroll = Scrollbar(self, command = self.listProg.yview)
		self.listProg.configure(yscrollcommand = scroll.set)

		self.listProg.grid(row = 0, column = 2, columnspan = 2, sticky = NE)
		scroll.grid(row = 0, column = 4, sticky = W)

		for item in ["CS", "CS with", "BIS", "SE", "Joints", ""]:
			self.listProg.insert(END, item)
		self.listProg.selection_set(END)
	def createTeamExpQuest(self):
		#Create widgets to ask Team Experience Questions
		#Team Experience
		lblStrAgr = Label(self, text= 'Team Experience:', font =('MS', 8, 'bold'))
		lblStrAgr.grid(row = 4, column = 0, rowspan = 2)
		#Radio Button
		lblStrAgr = Label (self, text = 'Strongly \n Agree', font = ('MS', 8, 'bold'))
		lblStrAgr.grid(row = 4, column = 4, rowspan = 2)
		#Our team worked together effectively
		lblStrAgr = Label(self, text= '1. Our team worked together effectively', font =('MS', 7))
		lblStrAgr.grid(row = 6, column = 0, rowspan = 2)
		#Radio Button
		lblStrAgr = Label (self, text = 'Agree', font = ('MS', 8, 'bold'))
		lblStrAgr.grid(row = 3, column = 5, rowspan = 2)
		#Our team produced good quality products
		lblStrAgr = Label(self, text= '2. Our team produced good quality products', font =('MS', 7))
		lblStrAgr.grid(row = 8, column = 0, rowspan = 2)
		#Radio Button
		lblStrAgr = Label (self, text = 'Partly \n Disagree', font = ('MS', 8, 'bold'))
		lblStrAgr.grid(row = 3, column = 6, rowspan = 2)
		#I enjoyed working in our team
		lblStrAgr = Label(self, text= '3. I enjoyed working in our team', font =('MS', 7))
		lblStrAgr.grid(row = 10, column = 0, rowspan = 2)
		#Radio Button
		lblStrAgr = Label (self, text = 'Strongly \n Disagree', font = ('MS', 8, 'bold'))
		lblStrAgr.grid(row = 3, column = 7, rowspan = 2)
		#Question 1
		self.varQ1 = IntVar()

		R1Q1 = Radiobutton (self, variable = self.varQ1, value = 4)
		R1Q1.grid (row = 6, column = 4)

		R2Q1 = Radiobutton (self, variable = self.varQ1, value = 3)
		R2Q1.grid (row = 6, column = 5) 

		R3Q1 = Radiobutton (self, variable = self.varQ1, value = 2)
		R3Q1.grid(row = 6, column = 6)

		R4Q1 = Radiobutton (self, variable = self.varQ1, value = 1)
		R4Q1.grid (row = 6, column = 7)
		#Question 2
		self.varQ2 = IntVar()
		R1Q2 = Radiobutton (self, variable = self.varQ2, value = 4)
		R1Q2.grid (row = 8, column = 4)

		R2Q2 = Radiobutton (self, variable = self.varQ2, value = 3)
		R2Q2.grid (row = 8, column = 5) 

		R3Q2 = Radiobutton (self, variable = self.varQ2, value = 2)
		R3Q2.grid(row = 8, column = 6)

		R4Q2 = Radiobutton (self, variable = self.varQ2, value = 1)
		R4Q2.grid (row = 8, column = 7)
		#Question 3
		self.varQ3 = IntVar()
		R1Q3 = Radiobutton (self, variable = self.varQ3, value = 4)
		R1Q3.grid (row = 10, column = 4)

		R2Q3 = Radiobutton (self, variable = self.varQ3, value = 3)
		R2Q3.grid (row = 10, column = 5) 

		R3Q3 = Radiobutton (self, variable = self.varQ3, value = 2)
		R3Q3.grid(row = 10, column = 6)

		R4Q3 = Radiobutton (self, variable = self.varQ3, value = 1)
		R4Q3.grid (row = 10, column = 7)

	def createProblems(self):
		#Create widgets to show Problems experienced

		lblProbl = Label(self, text= 'Problems:', font =('MS', 8, 'bold'))
		lblProbl.grid(row = 14, column = 0)

		lblProb2 = Label (self, text='Our team often experienced the ' + 
								'following problems (choose all that apply:')
		lblProb2.grid(row = 16, column = 0, columnspan = 6, sticky = W)

		self.varCB1 = IntVar()
		CB1 = Checkbutton(self, text = " Poor communication", variable = self.varCB1)
		CB1.grid (row = 18, column = 0, columnspan = 4, sticky = W)

		self.varCB2 = IntVar()
		CB2 = Checkbutton(self, text = " Lack of direction", variable = self.varCB2)
		CB2.grid (row = 19, column = 0, columnspan = 4, sticky = W)

		self.varCB3 = IntVar()
		CB3 = Checkbutton(self, text = " Disagreements Amongst Team", variable = self.varCB3)
		CB3.grid (row = 20, column = 0, columnspan = 4, sticky = W)

		self.varCB4 = IntVar()
		CB4 = Checkbutton(self, text = " Members Missed Meetings", variable = self.varCB4)
		CB4.grid (row = 18, column = 2, columnspan = 4, sticky = W)

		self.varCB5 = IntVar()
		CB5 = Checkbutton(self, text = " Members not contributing", variable = self.varCB5)
		CB5.grid (row = 19, column = 2, columnspan = 4, sticky = W)

		self.varCB6 = IntVar()
		CB6 = Checkbutton(self, text = " Members Not Motivated", variable = self.varCB6)
		CB6.grid (row = 20, column = 2, columnspan = 4, sticky = W)
	def createComments(self):
		#Sets up comments and name entries
		#Name
		lblComm = Label (self, text = 'Name (optional):', font = ('MS', 8, 'bold'))
		lblComm.grid(row = 21, rowspan = 2)

		self.entName = Entry(self)
		self.entName.grid(row = 21, column = 1, columnspan = 2, sticky = E)

		#Comments/Teamwork
		lblComm = Label (self, text = 'Comments about Teamwork', font = ('MS', 8, 'bold'))
		lblComm.grid(row = 22, rowspan = 2)

		self.txtComment = Text(self, height = 10, width = 40)

		scroll = Scrollbar(self, command= self.txtComment.yview)
		self.txtComment.configure(yscrollcommand=scroll.set)

		self.txtComment = Entry(self)
		self.txtComment.grid(row = 22, column = 1, columnspan = 2, sticky = E)

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
		#clears the questionnaire
		self.listProg.selection_clear(0, END)
		self.listProg.selection_set(END)

		self.varQ1.set(0)
		self.varCB1.set(0)
		self.varQ2.set(0)
		self.varCB2.set(0)
		self.varQ3.set(0)
		self.varCB3.set(0)
		self.varCB4.set(0)
		self.varCB5.set(0)
		self.varCB6.set(0)
		#add other buttons

		self.entName.delete(0, END)
		self.txtComment.delete(0, END)
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
							self.varQ1.get(), self.varQ2.get(), self.varQ3.get(),
							self.varCB1.get(), self.varCB2.get(), self.varCB3.get(),
							self.varCB4.get(), self.varCB5.get(), self.varCB6.get())
							#self.txtComment.get(0.0, END), self.entName.get())
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