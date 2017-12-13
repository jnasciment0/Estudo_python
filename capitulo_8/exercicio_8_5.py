"""definindo a função e argumento default"""
def decribe_city(cidade,pais='brasil'):
	print(cidade.title() + ", está localizada na(o) " + pais.title())

decribe_city('belém')
decribe_city('são paulo')
decribe_city('new york')
