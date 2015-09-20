import random
from Tkinter import *

def redrawAll(canvas):
    canvas.delete(ALL)
    drawGameboard(canvas)
    if (canvas.data["isGameOver"] == True):
        cx = canvas.data["canvasWidth"]/2
        cy = canvas.data["canvasHeight"]/2
        canvas.create_text(cx, cy, text="Game Over!", font=("Helvetica", 32, "bold"))

def drawGameboard(canvas):
    Gameboard = canvas.data["Gameboard"]
    rows = len(Gameboard)
    cols = len(Gameboard[0])
    for row in range(rows):
        for col in range(cols):
            drawCell(canvas, Gameboard, row, col)

def drawCell(canvas, Gameboard, row, col):
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
	score_text = "LETTER"

    canvas.create_rectangle(left, top, right, bottom, fill=color)
    #if (canvas.data["inDebugMode"] == True):
    canvas.create_text(left+cellSize/2,top+cellSize/2,
                           text=score_text,font=("Helvatica", 8, "bold"))

def init(canvas):
    loadGameboard(canvas)
    canvas.data["inDebugMode"] = False
    canvas.data["isGameOver"] = False
    redrawAll(canvas)

def loadGameboard(canvas):
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    Gameboard =  [ [ 6, 0, 0, 2, 0, 0, 0, 6, 0, 0, 0, 2, 0, 0, 6 ],
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

def run():
    # create the root and the canvas
    root = Tk()
    margin = 5
    cellSize = 60
    canvasWidth = 2*margin + 15*cellSize
    canvasHeight = 2*margin + 15*cellSize
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack()
    root.resizable(width=0, height=0)
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    canvas.data["margin"] = margin
    canvas.data["cellSize"] = cellSize
    canvas.data["canvasWidth"] = canvasWidth
    canvas.data["canvasHeight"] = canvasHeight
    canvas.data["rows"] = 15
    canvas.data["cols"] = 15
    init(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()
