import random
import sys, os, string, time, copy
from Tkinter import *
import Tkinter
tk = Tkinter

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

	def init(self,canvas,root):
		self.root = root
    		self.loc =self.dragged =0
		self.defaultcolor =canvas.itemcget (canvas.create_text (0, 0, text ="", tags ="DnD"), "fill")
    		self.loadGameboard(canvas)
		self.canvas = canvas
    		canvas.data["inDebugMode"] = False
    		canvas.data["isGameOver"] = False
		self.clickpos = []
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
		canvas.create_rectangle(950,0,1010,60, fill='grey', tags=('DnD', '0'))
		canvas.create_rectangle(950,60,1010,120, fill='grey', tags=('DnD', '1'))
		canvas.create_rectangle(950,120,1010,180, fill='grey', tags=('DnD', '2'))
		canvas.create_rectangle(950,180,1010,240, fill='grey', tags=('DnD', '3'))
		canvas.create_rectangle(950,240,1010,300, fill='grey', tags=('DnD', '4'))
		canvas.create_rectangle(950,300,1010,360, fill='grey', tags=('DnD', '5'))
		canvas.create_rectangle(950,360,1010,420, fill='grey', tags=('DnD', '6'))
		canvas.create_text (980, 30, text = '0', tags=('DnD', '0'))
		canvas.create_text (980, 90, text = '1', tags=('DnD', '1'))
		canvas.create_text (980, 150, text = '2', tags=('DnD', '2'))
		canvas.create_text (980, 210, text = '3', tags=('DnD', '3'))
		canvas.create_text (980, 270, text = '4', tags=('DnD', '4'))
		canvas.create_text (980, 330, text = '5', tags=('DnD', '5'))
		canvas.create_text (980, 390, text = '6', tags=('DnD', '6'))

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
       			self.canvas.itemconfig(CURRENT)
        		self.canvas.update_idletasks()
        		self.canvas.after(20)
		self.clickpos = [event.x/60, event.y/60]

	def down (self,  event):	
		self.loc =1
    		self.dragged =0
    		event.widget.bind ("<Motion>", self.motion)

  	def motion (self, event):
    		self.root.config (cursor ="exchange")
    		cnv = event.widget
    		cnv.itemconfigure (tk.CURRENT, fill ="blue")
    		xy = cnv.canvasx(event.x), cnv.canvasy(event.y)
    		points = event.widget.coords(tk.CURRENT)
    		anchors = copy.copy(points[:2])
    		for idx in range(len(points)):
       		 	mouse = xy[idx % 2]
        		zone = anchors[idx % 2]
        		points[idx] = points[idx] - zone + mouse
    			apply(event.widget.coords, [tk.CURRENT] + points)
  
  	def leave (self, event):
    		self.loc =0

  	def enter (self, event):
    		self.loc =1
    		if self.dragged == event.time:
     		 self.up (event)

  	def chkup (self, event):
    		event.widget.unbind ("<Motion>")
    		self.root.config (cursor ="")
    		self.target =event.widget.find_withtag (tk.CURRENT)
    		event.widget.itemconfigure (tk.CURRENT, fill = self.defaultcolor)
		points = [60*int(x / 60) for x in event.widget.coords(tk.CURRENT)]
    		if self.loc:
			event.widget.coords(tk.CURRENT, points[0], points[1], points[2], points [3])
      			self.up(event)
    		else:
    			self.dragged = event.time

  	def up (self, event):
    		event.widget.itemconfigure (tk.CURRENT, fill = "grey")
    		event.widget.unbind ("<Motion>")
    		if (self.target ==event.widget.find_withtag (tk.CURRENT)):
      			pass #"Select %s" %event.widget.itemcget (tk.CURRENT, "text")
    		else:
			pass
      			#event.widget.itemconfigure (tk.CURRENT, fill ="blue")
      			#self.root.update()
     			#time.sleep (.1)
      			#print "%s Drag-N-Dropped onto %s" \
        		#	%(event.widget.itemcget (self.target, "text"),
   			#event.widget.itemcget (tk.CURRENT, "text"))
      			#event.widget.itemconfigure (tk.CURRENT, fill =self.defaultcolor)


