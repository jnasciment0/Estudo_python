"""Argumento default"""
def make_shirt(tamanho = 'g', estampa='Eu amo Python'):
	print("O tamanho da sua blusa é: " + tamanho.upper())
	print("E a estampa é: '" + estampa.title() + "'")

"""Argumento posicionais"""
#make_shirt('gg')
"""Argumento nomeados"""
make_shirt('p','Eu amo a Thamires')
