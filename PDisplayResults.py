from Tkinter import *
from PResponse import PResponse

class DisplayResults (Frame):
	#GUI Setup

	def __init__(self, master):
		#initialize Questionnaire class

		Frame.__init__(self, master)
		self.pack
	def retrieveResponse(self):
		countAll = 0
		sumQ1SE = 0.0
		sumP5Joints = 0

		import shelve
		db=shelve.open('responsedb')
		respNo = len(db)

		for i in range (1, respNo):
			Ans = get.db(str(i))
			countAll +=1
			sumQ1All += Ans.q1
			sumQ2All += Ans.q2
			sumQ3All += Ans.q3
			sumP1All += Ans.pr1
			sumP2All += Ans.pr2
			sumP3All += Ans.pr3
			sumP4All += Ans.pr4
			sumP5All += Ans.pr5
			sumP6All += Ans.pr6
			if Ans.prog == "CS":
				countCS +=1
				sumQ1CS += Ans.q1
		db.close

		self.txtDisplay = Text(self, height = 14, width = 85)
		self.txtDisplay.tag_configure('boldfont', font =('MS', 8, 'bold'))
		self.txtDisplay.tag_configure('normfont', font = ('MS', 8))

		tabResults = ""
		tabResults += ("\t" + "\t" + "\t" + "\t")
		self.txtDisplay.insert(END, "Degree Programme" + tabResults + "ALL" + "\t"
								+ "CS" + "\t" + "CS with" + "\t" + "BIS" + "\t"
								+ "SE" + "\t" + "Joints" + '\n', 'boldfont')
		self.txtDisplay.insert(END, "Number of Responses:" + tabResults + str(countAll)
								+ "\t" + str(countCS) + "\t" + str(countCSwith) + "\t" +
								str(countBIS) + "\t" + str(countSE) + "\t" + str(countJoints)
								+'\n', 'normfont')
		#Add lines to display the team experience heading and explanation of the scores.
		if countAll > 0:
			Q1All = sumQ1All/countAll
			Q2All = sumQ2All/countAll
			Q3All = sumQ3All/countAll
			P1All = sumP1All*100/countAll
			P2All = sumP2All*100/countAll
			P3All = sumP3All*100/countAll

		else:
			Q1All = 0
			Q2All = 0
			Q3All = 0
			P1All = 0
			P2All = 0
			P3All = 0
		self.txtDisplay.insert(END, "1. Our team worked together effectively" + tabResults
								+ "%.1f" % Q1All + "\t %.1f" % Q1CS + "\t %.1f" % Q1CSwith
								+ "\t %.1f" % Q1BIS+ "\t %.1f" % Q1SE + "\t %.1f" %
								Q1Joints + '\n', 'normfont')
		#Repeat appropriately for the other two team experience questions. We can then add
		#a line to show the Problem Experienced heading

		self.txtDisplay.insert(END, "Poor Communication" + tabResults + "%d" % P1All 
 								+ "% \t" + "%d" % P1CS + "% \t" + "%d" % P1CSwith + "% \t" 
 								+ "%d" % P1BIS + "% \t" + "%d" % P1SE + "% \t" + "%d" % 
 								P1Joints + "% \n", 'normfont') 
		#Repeat appropriately for the other five problems
		self.txtDisplay['state'] = DISABLED
		self.txtDisplay.pack()

#Main
root = Tk()
root.title("Display Results")
app = DisplayResults(root)
root.mainloop()