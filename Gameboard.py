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
    #Draw normal cells
    for row in range(rows):
        for col in range(cols):
            drawCell(canvas, Gameboard, row, col, "white")
    #Draw "Triple word score" cells
    drawCell(canvas, Gameboard, 14, 14, "orange")
    drawCell(canvas, Gameboard, 0, 0, "orange")
    drawCell(canvas, Gameboard, 0, 14, "orange")
    drawCell(canvas, Gameboard, 14, 0, "orange")
    drawCell(canvas, Gameboard, 0, 7, "orange")
    drawCell(canvas, Gameboard, 7, 0, "orange")
    drawCell(canvas, Gameboard, 7, 14, "orange")
    drawCell(canvas, Gameboard, 14, 7, "orange")
    #Draw center cell
    drawCell(canvas, Gameboard, 7, 7, "red")
    #Draw "Double word score" cell
    drawCell(canvas, Gameboard, 1, 1, "pink")
    drawCell(canvas, Gameboard, 2, 2, "pink")
    drawCell(canvas, Gameboard, 3, 3, "pink")
    drawCell(canvas, Gameboard, 4, 4, "pink")
    drawCell(canvas, Gameboard, 14-1, 1, "pink")
    drawCell(canvas, Gameboard, 14-2, 2, "pink")
    drawCell(canvas, Gameboard, 14-3, 3, "pink")
    drawCell(canvas, Gameboard, 14-4, 4, "pink")
    drawCell(canvas, Gameboard, 1, 14-1, "pink")
    drawCell(canvas, Gameboard, 2, 14-2, "pink")
    drawCell(canvas, Gameboard, 3, 14-3, "pink")
    drawCell(canvas, Gameboard, 4, 14-4, "pink")
    drawCell(canvas, Gameboard, 14-1, 14-1, "pink")
    drawCell(canvas, Gameboard, 14-2, 14-2, "pink")
    drawCell(canvas, Gameboard, 14-3, 14-3, "pink")
    drawCell(canvas, Gameboard, 14-4, 14-4, "pink")
    #Draw "Triple letter score" cell
    drawCell(canvas, Gameboard, 5, 1, "green")
    drawCell(canvas, Gameboard, 14-5, 1, "green")
    drawCell(canvas, Gameboard, 5, 14-1, "green")
    drawCell(canvas, Gameboard, 14-5, 14-1, "green")
    drawCell(canvas, Gameboard, 1, 5, "green")
    drawCell(canvas, Gameboard, 1, 14-5, "green")
    drawCell(canvas, Gameboard, 14-1, 5, "green")
    drawCell(canvas, Gameboard, 14-1, 14-5, "green")
    drawCell(canvas, Gameboard, 5, 5, "green")
    drawCell(canvas, Gameboard, 14-5, 5, "green")
    drawCell(canvas, Gameboard, 5, 14-5, "green")
    drawCell(canvas, Gameboard, 14-5, 14-5, "green")
    drawCell(canvas, Gameboard, 5, 5, "green")
    drawCell(canvas, Gameboard, 5, 14-5, "green")
    drawCell(canvas, Gameboard, 14-5, 5, "green")
    drawCell(canvas, Gameboard, 14-5, 14-5, "green")
    #Draw "Double letter score" cell
    drawCell(canvas, Gameboard, 3, 0, "blue")
    drawCell(canvas, Gameboard, 0, 3, "blue")
    drawCell(canvas, Gameboard, 0, 14-3, "blue")
    drawCell(canvas, Gameboard, 14-3, 0, "blue")
    drawCell(canvas, Gameboard, 3, 14, "blue")
    drawCell(canvas, Gameboard, 14, 3, "blue")
    drawCell(canvas, Gameboard, 14, 14-3, "blue")
    drawCell(canvas, Gameboard, 14-3, 14, "blue")
    drawCell(canvas, Gameboard, 6, 6, "blue")
    drawCell(canvas, Gameboard, 14-6, 6, "blue")
    drawCell(canvas, Gameboard, 6, 14-6, "blue")
    drawCell(canvas, Gameboard, 14-6, 14-6, "blue")
    drawCell(canvas, Gameboard, 2, 6, "blue")
    drawCell(canvas, Gameboard, 2, 14-6, "blue")
    drawCell(canvas, Gameboard, 14-2, 6, "blue")
    drawCell(canvas, Gameboard, 14-2, 14-6, "blue")
    drawCell(canvas, Gameboard, 6, 2, "blue")
    drawCell(canvas, Gameboard, 6, 14-2, "blue")
    drawCell(canvas, Gameboard, 14-6, 2, "blue")
    drawCell(canvas, Gameboard, 14-6, 14-2, "blue")
    drawCell(canvas, Gameboard, 3, 7, "blue")
    drawCell(canvas, Gameboard, 7, 3, "blue")
    drawCell(canvas, Gameboard, 14-3, 7, "blue")
    drawCell(canvas, Gameboard, 7, 14-3, "blue")



def drawCell(canvas, Gameboard, row, col, color):
    margin = canvas.data["margin"]
    cellSize = canvas.data["cellSize"]
    left = margin + col * cellSize
    right = left + cellSize
    top = margin + row * cellSize
    bottom = top + cellSize
    canvas.create_rectangle(left, top, right, bottom, fill=color)
    #if (canvas.data["inDebugMode"] == True):
    canvas.create_text(left+cellSize/2,top+cellSize/2,
                           text=str(Gameboard[row][col]),font=("Helvatica", 14, "bold"))

def init(canvas):
    loadGameboard(canvas)
    canvas.data["inDebugMode"] = False
    canvas.data["isGameOver"] = False
    canvas.data["snakeDrow"] = 0
    canvas.data["snakeDcol"] = -1 # start moving left
    canvas.data["ignoreNextTimerEvent"] = False
    redrawAll(canvas)

def loadGameboard(canvas):
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    Gameboard = [ ]
    for row in range(rows): Gameboard += [[0] * cols]
    Gameboard[rows/2][cols/2] = 1
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
