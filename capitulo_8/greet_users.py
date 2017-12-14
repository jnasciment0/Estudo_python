def greet_users(names):
	"""Exibe uma saudação simples a cada usuario da lista"""
	for name in names:
		msg = "hello, " + name.title() + "!"
		print(msg)


usernames = ['jasson','alan','robinho']
greet_users(usernames)