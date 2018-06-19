from collections import OrderedDict

glossario = OrderedDict()

glossario['jen']='python'
glossario['sarah']='c'
glossario['edward']='ruby'
glossario['phil']='python'

for key, value in glossario.items():
	print("Qual a sua liguagem de programa você mais gosata " + key.title() + "?")
	print("Eu " + key.title() + " goste de " + value.title() + "\n")