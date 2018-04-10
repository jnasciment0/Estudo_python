magicos_nomes = ['Jasson','Huding', 'Mrs. M']
nomes_novos = []

def show_magiccians(magicos_nomes):
	for magicos_nome in magicos_nomes:
		print("Apresento a vocês os magicos: \n" + magicos_nome.title())

def make_great(magicos_nomes,nomes_novos):
	
	while magicos_nomes:
		recebe_nome = magicos_nomes.pop()
		##print("magic: " +recebe_nome )
		nomes_novos.append('O grande ' + recebe_nome)
	
	for nomes_novo in nomes_novos:
		print("Apresento : "+ nomes_novo)

show_magiccians(magicos_nomes)
make_great(magicos_nomes,nomes_novos)