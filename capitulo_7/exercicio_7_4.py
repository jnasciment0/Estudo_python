#mensagem para o input
mensage = "Por favor informe os ingredientes de sua pizza"
mensage += "\n(Caso tenha terminado de inserir os ingredientes para sair digite quit): "
#lista vazia de ingredientes
ingredientes = []

while True:
	ingrediente = input(mensage)

	#condição para finalizar 
	if ingrediente == 'quit':
		print("Aguarde em quanto finalizamos sua pizza")
		break
	else:
		#adicionando os ingredientes na lista vazia
		if ingrediente not in ingredientes:
			ingredientes.append(ingrediente)
		#listando os ingridientes
		print("Os ingredientes de sua são:")
		for value in ingredientes:
			print("\t"+value.title())


