numero = input("Informe um numero para saber se é multiplo de 10: ")
numero = int(numero)

if numero % 10 == 0:
	print("\nO valor " +str(numero) + " é multiplo de 10")
else:
	print("\n O valor " + str(numero) + " não é multiplo de 10")