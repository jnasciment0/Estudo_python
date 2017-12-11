convidados = ['Jasson', 'Carol', 'Thiago']
print('Lista de convidados \n'+str(convidados))

print("Ola " + convidados[0] + " Gostariamos de lhe convidar pra um jantar")
print("Ola " + convidados[1] + " Gostariamos de lhe convidar pra um jantar")
print("Ola " + convidados[2] + " Gostariamos de lhe convidar pra um jantar")


nao_presenca = convidados.pop(0)

print("\n Ola, Gostariamos de informar que Sr(a)" + nao_presenca +" não ira participar do jantar")
print('Lista de convidados \n'+str(convidados)+ "\n")

convidados.insert(0,'Wesley')
print('Nova Lista de convidados \n'+str(convidados)+ "\n")
print("Ola " + convidados[0] + " Gostariamos de lhe convidar pra um jantar")
print("Ola " + convidados[1] + " Gostariamos de lhe convidar pra um jantar")
print("Ola " + convidados[2] + " Gostariamos de lhe convidar pra um jantar")
