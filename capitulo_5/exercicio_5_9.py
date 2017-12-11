lista_nomes = ['jasson']
# ['jasson', 'wesley', 'luiz', 'matheus', 'robinho', 'admin']

if lista_nomes:
	for lista_nome in lista_nomes:
		if lista_nome == 'admin':
			print("Olá admin, gostaria de ver um relatório de status?")
		else:
			print("Olá " + lista_nome + ", obrigado por fazer login novamente")
else:
	print("Precisamos encontrar alguns usuários")