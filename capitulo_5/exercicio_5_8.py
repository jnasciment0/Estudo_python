lista_nomes = ['jasson', 'wesley', 'luiz', 'matheus', 'robinho', 'admin']

for lista_nome in lista_nomes:
	if lista_nome == 'admin':
		print("Olá admin, gostaria de ver um relatório de status?")
	else:
		print("Olá " + lista_nome + ", obrigado por fazer login novamente")