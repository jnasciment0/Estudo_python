convidados = ['Jasson', 'Carol', 'Thiago']
print(convidados)

#inserindo um novo convidado no inicio
convidados.insert(0,'Wesley')
print(convidados)

#inserindo um novo convidado no meio
convidados.insert(2,'Luiz')
print(convidados)

#inserindo um novo convidado no final
convidados.append('Matheus')
print(convidados)

print("Ola " + convidados[0] + " Gostariamos de lhe convidar pra um jantar")
print("Ola " + convidados[1] + " Gostariamos de lhe convidar pra um jantar")
print("Ola " + convidados[2] + " Gostariamos de lhe convidar pra um jantar")
print("Ola " + convidados[3] + " Gostariamos de lhe convidar pra um jantar")
print("Ola " + convidados[4] + " Gostariamos de lhe convidar pra um jantar")
print("Ola " + convidados[5] + " Gostariamos de lhe convidar pra um jantar")

#removendo alguns convidados

removendo_convidados = convidados.pop(0)
print("O convidado " + removendo_convidados + " foi removido da lista de convidados")
print(str(convidados) + "\n")

removendo_convidados = convidados.pop(1)
print("O convidado " + removendo_convidados + " foi removido da lista de convidados")
print(str(convidados) + "\n")

removendo_convidados = convidados.pop(2)
print("O convidado " + removendo_convidados + " foi removido da lista de convidados")
print(str(convidados) + "\n")

removendo_convidados = convidados.pop(2)
print("O convidado " + removendo_convidados + " foi removido da lista de convidados")
print(str(convidados) + "\n")

print("Ola " + convidados[0] + " Gostariamos de lhe convidar pra um jantar")
print("Ola " + convidados[1] + " Gostariamos de lhe convidar pra um jantar")

#deletando os 2 ultimos convidados
del convidados[0]
print("Removendo o ultimos convidados: " + str(convidados))

del convidados[0]
print("Removendo o ultimos convidados: " + str(convidados))

print("Festa Cancelada!")