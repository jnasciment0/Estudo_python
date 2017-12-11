current_users = ['jasson', 'wesley', 'luiz', 'matheus', 'robinho', 'admin']

new_users = ['Jasson', 'admin' , 'carol', 'alan']

for new_user in new_users:
	padrao_users = new_user.lower()

	if padrao_users in current_users:
		print("Desculpe, usuário " +padrao_users +" já estar logado!")
	else: 
		print("Os usurário disponiveis para logar é: " + padrao_users)

