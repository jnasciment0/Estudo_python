sandwich_orders = ['hambuguer','hotdog','x-egges','misto','cachorrao','x-tudo']
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print("Preparando o seu sanduiche de " + sandwich.title())
	finished_sandwiches.append(sandwich)

print("\nOs lanches prontos são")
for finished_sandwiche in finished_sandwiches:
	print("Saindo um(a) " + finished_sandwiche.title())