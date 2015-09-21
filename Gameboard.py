import random
from Tkinter import *


class Gameboard():   
	def redrawAll(self,canvas):
    		canvas.delete(ALL)
    		self.drawGameboard(canvas)
    		if (canvas.data["isGameOver"] == True):
        		cx = canvas.data["canvasWidth"]/2
        		cy = canvas.data["canvasHeight"]/2
        		canvas.create_text(cx, cy, text="Game Over!", font=("Helvetica", 32, "bold"))

	def drawGameboard(self,canvas):
  		Gameboard = canvas.data["Gameboard"]
    		rows = len(Gameboard)
    		cols = len(Gameboard[0])
   		for row in range(rows):
        		for col in range(cols):
            			self.drawCell(canvas, Gameboard, row, col)

	def drawCell(self,canvas, Gameboard, row, col):
    		margin = canvas.data["margin"]
    		cellSize = canvas.data["cellSize"]
    		left = margin + col * cellSize
    		right = left + cellSize
    		top = margin + row * cellSize
    		bottom = top + cellSize
    		color = "white" 	
    		score_text = ""
    		if (Gameboard[row][col] == 1):
			color = "red" 
			score_text = ":)"
    		if (Gameboard[row][col] == 2):
			color = "cyan" 	
			score_text = "Double \n letter \n score"
    		if (Gameboard[row][col] == 3):
			color = "green" 
			score_text = "Triple \n letter \n score"	
    		if (Gameboard[row][col] == 4):
			color = "pink" 	
			score_text = "Double \n word \n score"	
    		if (Gameboard[row][col] == 6):
			color = "orange"
			score_text = "Triple \n word \n score"
		if (Gameboard[row][col] == 10):
			color = "grey"
			score_text = self.Gameboard_letter[row][col]

    		canvas.create_rectangle(left, top, right, bottom, fill=color)
    		canvas.create_text(left+cellSize/2,top+cellSize/2,
                           text=score_text,font=("Helvatica", 8, "bold"))

	def init(self,canvas):
    		self.loadGameboard(canvas)
		self.canvas = canvas
    		canvas.data["inDebugMode"] = False
    		canvas.data["isGameOver"] = False
    		self.redrawAll(canvas)
		self.Gameboard_letter =  [["","","","","","","","","","","","","","",""],
			["","","","","","","","","","","","","","",""],
			["","","","","","","","","","","","","","",""],
			["","","","","","","","","","","","","","",""],
			["","","","","","","","","","","","","","",""],
			["","","","","","","","","","","","","","",""],
			["","","","","","","","","","","","","","",""],
			["","","","","","","","","","","","","","",""],
			["","","","","","","","","","","","","","",""],
			["","","","","","","","","","","","","","",""],
			["","","","","","","","","","","","","","",""],
			["","","","","","","","","","","","","","",""],
			["","","","","","","","","","","","","","",""],
			["","","","","","","","","","","","","","",""],
			["","","","","","","","","","","","","","",""]]

	def loadGameboard(self,canvas):
   		rows = canvas.data["rows"]
    		cols = canvas.data["cols"]
    		self.Gameboard = Gameboard =  [ [ 6, 0, 0, 2, 0, 0, 0, 6, 0, 0, 0, 2, 0, 0, 6 ],
     	           [ 0, 4, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 4, 0 ],
       	           [ 0, 0, 4, 0, 0, 0, 2, 0, 2, 0, 0, 0, 4, 0, 0 ],
 		   [ 2, 0, 0, 4, 0, 0, 0, 2, 0, 0, 0, 4, 0, 0, 2 ],
		   [ 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0 ],
		   [ 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0 ],
		   [ 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0 ],
		   [ 6, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 6 ],
		   [ 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0 ],
                   [ 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0 ],
 		   [ 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0 ],
		   [ 2, 0, 0, 4, 0, 0, 0, 2, 0, 0, 0, 4, 0, 0, 2 ],
		   [ 0, 0, 4, 0, 0, 0, 2, 0, 2, 0, 0, 0, 4, 0, 0 ],
		   [ 0, 4, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 4, 0 ],
		   [ 6, 0, 0, 2, 0, 0, 0, 6, 0, 0, 0, 2, 0, 0, 6 ],
                ]
    		canvas.data["Gameboard"] = Gameboard


	#put tiles on the game board
	def put_tiles(self, word, x ,y , horiz_or_verti): #1 for horizontal, 0 for vertical
		for i in range(len(list(word))):
			if (horiz_or_verti == 0): 	
				self.Gameboard_letter[x+i][y] = list(word)[i]
				self.Gameboard[x+i][y] = 10
			else:
				self.Gameboard_letter[x][y+i] = list(word)[i]
				self.Gameboard[x][y+i] = 10

	#check if action is possible
	def check_if_possible(self, word, x ,y , horiz_or_verti):
		max_value = 0
		for i in range(len(list(word))):
			if (horiz_or_verti == 0):
				if (self.Gameboard[x+i][y] > max_value):
					max_value = self.Gameboard[x+i][y]
			else:
				if (self.Gameboard[x+i][y] > max_value):
					self.Gameboard[x][y+i] = 10	
		if (max_value==10):
			return True
		else:
			return False

	def click(self, event):
    		if self.canvas.find_withtag(CURRENT):
       			self.canvas.itemconfig(CURRENT, fill="blue")
        		self.canvas.update_idletasks()
        		self.canvas.after(200)
        		print event.x
			print event.y

