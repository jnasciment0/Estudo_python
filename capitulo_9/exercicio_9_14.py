import random 

class Die():
	"""docstring for ClassName"""
	def __init__(self, sides = 6):
		self.sides = sides

	def dado(self):
		fvalue = 0
		for qts in range(0,self.sides):
			value = random.randint(1,6)
			fvalue = fvalue + value
		return fvalue

	
jogar_dados = Die()

print(jogar_dados.dado())