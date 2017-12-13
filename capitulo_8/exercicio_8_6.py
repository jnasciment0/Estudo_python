def city_country(cidade,pais):
	cidade_pais = cidade + ', ' + pais
	return cidade_pais.title()

resultado = city_country('belém','brasil')
print(resultado)
