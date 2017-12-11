#começa com os usuario que precisam ser verificados
# e com uma lista vazia para armazenar os usuario confirmados
unconfirmed_users = ['alice','brian','candace']
confirmed_users=[]

#verificando cada usuario ate que não haja mais usuarios não confirmados
#transfere cada usuario verificando para a lista de usuarios confirmados

while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print("Verifying user: " +current_user.title())
	confirmed_users.append(current_user)

#exibe todos os usuarios confirmados
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())