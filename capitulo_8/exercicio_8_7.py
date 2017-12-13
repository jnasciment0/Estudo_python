def make_album(nome_artista,album_artista,numero_faixa=''):
	cd_music = {'nome':nome_artista,'album':album_artista}
	if numero_faixa:
		cd_music['faixa'] = numero_faixa
	return cd_music

musica = make_album('jimi','hendrix',9)
print(musica)
musica = make_album('simone e simara','amigas')
print(musica)
musica = make_album('caju e castanha','rico e pobre')
print(musica)