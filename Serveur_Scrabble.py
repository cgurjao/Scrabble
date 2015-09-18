import random
from Tkinter import *
from tkMessageBox import askokcancel           

class Quitter(Frame):                          
    def __init__(self): 
	self.serv = Serv = Serveur()        
        Frame.__init__(self, None)
        self.pack()
   	fields = 'Word Suggested',
	self.word = ''
    	vars = self.makeform(self, fields)
    	Button(self, text='Fetch', command=(lambda v=vars: self.fetch_and_run(v))).pack(side=LEFT)
    	self.bind('<Return>', (lambda event, v=vars: self.fetch_and_run(v)))
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(expand=YES, fill=BOTH, side=LEFT)

    def quit(self):
        ans = askokcancel('Verify exit', "Really quit?")
        if ans: Frame.quit(self)


    def fetch_and_run(self,variables):
    	for variable in variables:
       		self.word = variable.get()
	
	if (self.serv.check_dict(self.word)==False):
		print self.word + " doesn't exist, try another word!"
    		for variable in variables:
       			self.word = variable.get()
	else :
		print self. word +  " was found in the dictionnary, well done!"
		print "Available letters : " 
		print self.serv.letter_holderPL1
		
	
    def makeform(self,root, fields):
    	form = Frame(root)                              
    	left = Frame(form)
    	rite = Frame(form)
    	form.pack(fill=X) 
    	left.pack(side=LEFT)
    	rite.pack(side=RIGHT, expand=YES, fill=X)
    	variables = []
    	for field in fields:
        	lab = Label(left, width=15, text=field)
        	ent = Entry(rite)
       		lab.pack(side=TOP)
        	ent.pack(side=TOP, fill=X)
        	var = StringVar()
        	ent.config(textvariable=var)
        	var.set('enter here')
        	variables.append(var)
        return variables


    def run(self):
	while (len(self.serv.tiles) != 0):
    		Tk().mainloop()

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
				'z']
			print "=> Done!"
			print "Initializing letter holders"
			self.letter_holderPL1 = []
			self.letter_holderPL2 = []
			self.pick_tiles(self.letter_holderPL1)
			self.pick_tiles(self.letter_holderPL2)
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

Quitter().run()


