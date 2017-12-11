pessoa1 ={'nome':'jasson' ,'idade':28,}
pessoa2 ={'nome':'wesley' ,'idade':35,}
pessoa3 ={'nome':'matheus','idade':24,}

peoples = [pessoa1, pessoa2, pessoa3]

for people in peoples:
	print("Nome: " + people['nome'].title() + " e idade: " + str(people['idade']))
