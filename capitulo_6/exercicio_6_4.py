glossario = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python'
}

for key, value in glossario.items():
	print("Qual a sua liguagem de programa você mais gosata " + key.title() + "?")
	print("Eu " + key.title() + " goste de " + value.title() + "\n")