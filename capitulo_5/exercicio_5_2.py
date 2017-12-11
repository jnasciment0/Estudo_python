nome = 'jasson'

print("Teste de igualdade")
print(nome == 'jasson')

print("\nTeste de não igualdade")
print(nome == 'manito')

print("\n############################\n")
print("Carros")
cars = ['audi', 'bmw','subaru','toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

print("\n############################\n")
print("Teste numerico")

idade = 18
print("\nIgualdade 18 == 18")
print(idade == 18)

print("\nNão Igualdade 18 == 20")
print(idade == 20)

print("\nMaior 18 > 20")
print(idade > 20)

print("\nMenor 18 < 15")
print(idade < 15)

print("\nMaior igual 18 >=18")
print(idade >=18)

print("\nMenor igual 18 <=17")
print(idade <=17)

print("\n############################\n")
print("Teste usando and e or \n")

idade1 = 16
idade2 = 18

if idade1 <= 16 and idade2 >= 18:
	print("Já pode trabalhar e votar ")
else:
	print("Vais estudar!")



print("\n############################\n")
print("Verificando se o nome está na lista \n")

nomes = ['Jasson', 'Carol', 'Matheus']
encontra = 'Jasson'
print("O nome foi encontrado na lista? ")
print(encontra in nomes)


print("\n############################\n")
print("Verificando se o nome não está na lista \n")

procurar = 'Luiz'

if procurar not in nomes:
	print(procurar + ", não contrando!")