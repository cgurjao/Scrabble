import random
from Tkinter import *
from tkMessageBox import askokcancel      
from Gameboard import *

class Scrabble_GUI(Frame):                          
    def __init__(self): 
	self.serv = Serv = Serveur() 
        Frame.__init__(self, None)
        self.pack()
	self.root = Tk()
   	fields = 'Word Suggested',
	self.word = ''
	print "Available letters : "  #To display first available letters in the holder
	print self.serv.letter_holderPL1
    	Button(self.root, text='Fetch', command=(lambda v=vars: self.fetch_and_run(v))).pack(side=RIGHT) #"Fetch suggested word" button
    	self.bind('<Return>', (lambda event, v=vars: self.fetch_and_run(v)))
        widget2 = Button(self.root, text='Quit', command=self.quit) #"Quit" button
	widget2.pack(side=RIGHT)
    	margin = 0 #Define the space between each cell of the gameboard
    	cellSize = 60 #Size (in pixels) of the cells 
    	canvasWidth = 1100 # Width of the window
    	canvasHeight = 910 # Height of the window
    	self.canvas = Canvas(self.root, width=canvasWidth, height=canvasHeight)
    	self.canvas.pack()
    	self.root.resizable(width=0, height=0)
   	 # Store canvas in root and in canvas itself for callbacks
    	self.root.canvas = self.canvas.canvas = self.canvas
    	# Set up canvas data and call init
    	self.canvas.data = { }
    	self.canvas.data["margin"] = margin
    	self.canvas.data["cellSize"] = cellSize
   	self.canvas.data["canvasWidth"] = canvasWidth
    	self.canvas.data["canvasHeight"] = canvasHeight
    	self.canvas.data["rows"] = 15
    	self.canvas.data["cols"] = 15

    def quit(self):
        ans = askokcancel('Verify exit', "Really quit?") #To make sure the player want to exit the game
        if ans: Frame.quit(self)	

    def fetch_and_run(self,variables): #Each time the user clicks on "Fetch", the program will... 
	horiz_or_vert = self.GM.check_aligned()  #...Check if the tiles are aligned and determine if the word is put horizontally or vertically (resp, horiz_or_vert will be equal to 0 and 1)
	self.word = self.GM.check_over_tiles(horiz_or_vert) #... Check Scrabble's basic rule for playing : new words must use older words' letter
	if horiz_or_vert == 2:
		print "Not aligned!!!"
		return 0	#...get the suggested word from the gameboard 
	if (self.serv.check_dict(self.word)==False):   #...Check if the word exists in the dictionnary
		print self.word + " doesn't exist, try another word!"
    		return 0
	else :	#If all the previous conditions are met, the algorithm will...
		print self. word +  " was found in the dictionnary, well done!" 
		self.serv.scorePL1 = self.serv.get_score(self.word, self.serv.scorePL1)  #...Calculate and update the player's score
		self.GM.check_other_words()
		print "Your score : "
		print self.serv.scorePL1
		self.serv.remove_used_letters(self.word, self.serv.letter_holderPL1)	#...Remove used letters from the letter holder 
		initialpos = self.GM.get_initialpos(horiz_or_vert)
		self.GM.put_tiles(self.word, initialpos[1], initialpos[0], horiz_or_vert) #...Put the suggested word on the gameboard "for real" (i.e. the player won't be able to move them anymore)
		self.serv.pick_tiles(self.serv.letter_holderPL1) 	#...Fill the letter holder with other tiles
		self.GM.drawGameboard(self.canvas) 
		self.GM.associate_letter_tiles(self.serv.letter_holderPL1)
		self.GM.draw_letterHolder(self.canvas, self.root, self.serv.letter_holderPL1) #...Print the new updated letter holder on
		print "Available letters : "  #To display first available letters in the holder
		print self.serv.letter_holderPL1

    def run(self):
   	# create the root and the canvas
	self.GM = Gameboard()
    	self.GM.init(self.canvas, self.root)
	self.canvas.bind("<Button-1>", self.GM.click) #Bind button to function call
    	self.canvas.tag_bind ("DnD", "<ButtonPress-1>", self.GM.down) #Bind button to function call
    	self.canvas.tag_bind ("DnD", "<ButtonRelease-1>", self.GM.chkup) #Bind button to function call
    	self.canvas.tag_bind ("DnD", "<Enter>", self.GM.enter) #Bind button to function call
    	self.canvas.tag_bind ("DnD", "<Leave>", self.GM.leave) #Bind button to function call
	self.GM.associate_letter_tiles(self.serv.letter_holderPL1) #Diplay first letter holder
	self.root.mainloop()

class Serveur:
	def __init__(self):
		global DICO
		global NB_MOTS
		try:
			print "Reading dictionnary..."
			f=open("Mots_Scrabble.txt","r")
			f.readline()
			self.DICO = DICO=f.readlines()
			NB_MOTS=len(DICO)
			num_ligne=1
			chaine=""
			for ligne in DICO:
				col=ligne
				chaine+=str(col[0])
				num_ligne+=1
			f.close()
			print "=> Done! Number of words in the dictionnary : ", NB_MOTS
			#Initializing gameboard
			print "Initializing gameboard..."
			self.gameboard = [[0 for i in range(15)] for j in range(15)]
			print "=> Done!"
			#Initializing Scrabble bag
			print "Initializing Scrabble bag..."
			self.scores = {"0" : 0,"A": 1,"B": 3,"C": 3,"D": 2,"E": 1,"F": 4,"G": 2,
        			  "H": 4,"I": 1,"J": 8,"K": 5,"L": 1,"M": 3,"N": 1,"O": 1,
				  "P": 3,"Q": 10,"R": 1,"S": 1,"T": 1,"U": 1,"V": 4,"W": 4,
				  "X": 8,"Y": 4,"Z": 10}
			self.tiles = ['0','0',
				'A','A','A','A','A','A','A','A','A',
				'B','B',
				'C','C',
				'D','D','D','D',
				'E','E','E','E','E','E','E','E','E','E','E','E',
				'F', 'F',
				'G','G','G',
				'H','H',
				'I','I','I','I','I','I','I','I','I',
				'J',
				'K',
				'L','L','L','L',
				'M','M',
				'N','N','N','N','N','N',
				'O','O','O','O','O','O','O','O',
				'P','P',
				'Q',
				'R','R','R','R','R','R',
				'S','S','S','S',
				'T','T','T','T','T','T',
				'U','U','U','U',
				'V','V',
				'W','W',
				'X',
				'Y','Y',
				'Z']
			print "=> Done!"
			print "Initializing letter holders"
			self.letter_holderPL1 = []
			self.scorePL1 = 0
			self.pick_tiles(self.letter_holderPL1)
			print "=> Done!"
		#sinon le serveur se ferme
		except IOError:
			print "DICO.txt can't be found :'( ! \n"
			exit(1)

	#Fill letter holder and empty scrabble bag
	def pick_tiles(self, letter_holder):
		for i in range(7-len(letter_holder)):
				rand_num = random.randrange(len(self.tiles))
				letter_holder.append(self.tiles[rand_num])
				self.tiles.pop(rand_num)

	#Check if word is in the dictionnary
	def check_dict(self, given_word):
		return given_word + "\r\n" in self.DICO

	#Check if word can be made with the letters available in the holder!
	def usable_letters(self, given_word, letter_holder):
		print "In usable_letter"
		print given_word
		print letter_holder
		initial_len = len(letter_holder)
		for i in range(len(list(given_word))):
			for j in range(len(letter_holder)):
				if (letter_holder[j] == list(given_word)[i]):
					letter_holder.pop(j)
					break
		if ((initial_len - len(letter_holder)) == len(given_word)):
			return True
		else:
			return False
	#Remove used letters
	def remove_used_letters(self, given_word, letter_holder):
    		A = set(letter_holder).intersection(list(given_word))
		for i in range(len(list(A))):
			for j in range(len(letter_holder)):
				if (letter_holder[j] == list(A)[i]):
					letter_holder.pop(j)
					break
		return letter_holder

	#New score
	def get_score(self, given_word, score):
    		for i in range(len(list(given_word))):
			score = score + self.scores[list(given_word)[i]]
		return score		
		

Scrabble_GUI().run()


