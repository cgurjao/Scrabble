import random

class Serveur:
	def __init__(self):
		global DICO
		global NB_MOTS
		try:
			print "Reading dictionnary..."
			f=open("Mots_Scrabble.txt","r")
			f.readline()
			DICO=f.readlines()
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

	#Run game!
	def run(self):
		self.pick_tiles(self.letter_holderPL1)
		self.pick_tiles(self.letter_holderPL2)
		while (len(self.tiles) != 0): #Game running till the Scrabble bag is empty
			print "yolo"

Serv = Serveur()
Serv.run()
