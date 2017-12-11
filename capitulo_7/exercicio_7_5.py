#mensagem para o input
mensage = "Para saber qual ira pagar na entrada do cinema por favor digite sua idade"
mensage += "\n(Caso tenha recebido o valor digite (quit) para sair): "

while True:

	idade = input(mensage)
	
	#condição para finalizar 
	if idade == 'quit':
		print("Imprimindo o seu ingresso")
		break
	else:
		idade = int(idade)
		if idade < 3:
			print("A entrada sera gratuita.")
		elif idade > 3 and idade < 12:
			print("O ingresso custa R$ 10,00")
		elif idade > 12:
			print("O ingresso custa R$ 15,00")

	
