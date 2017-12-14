#comeca com alguns designs que devem ser impressos
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

#simula a impressao de cada design, ate que não haja mais nenhum
#transfere cada design para completed_models apos a impressao

while unprinted_designs:
	current_design = unprinted_designs.pop()

	#simula a criacao de uma pessao 3d apartir do design
	print("Printing model: " + current_design)
	completed_models.append(current_design)

#exibe todos os modelos finalizados
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)