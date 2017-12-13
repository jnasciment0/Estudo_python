def make_album(nome_artista,album_artista,numero_faixa=''):
	cd_music = {'nome':nome_artista,'album':album_artista}
	if numero_faixa:
		cd_music['faixa'] = numero_faixa
	return cd_music

while True:
	print("Insira o nome do artista, o album e a faixa (não obrigatoria)")
	print("(Para sair do programa digite 'quit')")

	n_artista = input("Nome do artista: ")
	if n_artista == 'quit':
		break
	
	alb_artista = input("Nome do Album: ")
	if alb_artista == 'quit':
		break
	
	num_faixa = input("Numero da faixa")
	if num_faixa == 'quit':
		break

	musica = make_album(n_artista,alb_artista,num_faixa)
	print(musica)
	