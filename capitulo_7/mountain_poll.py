responses={}
#definindo uma flag para indicar que a enquete esta ativa
polling_active = True

while polling_active:
	#pede o nome da pessoa e a resposta
	name = input("\nQual o seu nome? ")
	response = input("Qual montanha você gostaria de escalar algum dia.? ")

	#armazena a resposta no dicionario
	responses[name]=response

	#descobre se a outra pessoa vai responder a enquete
	repeat = input("Você gostaria de responder novamente a enquete? (sim/nao) ")
	if repeat == 'nao':
		polling_active = False

#a enquete foi concluida. mostra os resultados.
print("\n -- Enquete encerrada --")
for name, response in responses.items():
	print(name.title() + " gostaria de escalar " + response.title() + ".")