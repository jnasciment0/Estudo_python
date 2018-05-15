class Dog():
	"""Uma tentativa simples de modelas um cachorro"""

	def __init__(self, name, age):
		"""Inicializa os atributos name e age"""
		self.name = name
		self.age = age

	def sit(self):
		"""Simul um cachorro sentado em respota a um comando"""
		print(self.name.title() + "is now sitting.")

	def roll_over(self):
		"""Simul um cachorro rolando em respota a um comando"""
		print(self.name.title() + "rolled over!")


my_dog = Dog('willie',9)
your_dog = Dog('lucy',3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nMy dog's name is " + your_dog.name.title() + ".")
print("My dog is " + str(your_dog.age) + " years old.")
my_dog.roll_over()