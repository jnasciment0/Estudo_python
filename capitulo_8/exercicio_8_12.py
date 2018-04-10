def sanduiches(num_list,*qnt_sandus):
	print("\nLista dos sanduiche pedidos de numero: " + str(num_list))
	for qnt_sandu in qnt_sandus:
		print("-" + qnt_sandu)

sanduiches(1,'misto','hamburgue','x-eggs')
sanduiches(2,'x-tudo','hot-dog','x-calabreza','x-frango')
sanduiches(3,'cachorro-quente','americano','x-file','cachorrao','x-hot')
