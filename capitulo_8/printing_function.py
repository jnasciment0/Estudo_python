def print_models(unprinted_designs, completed_models):
	"""Simula a impressão de casa design, ate que não haja mais nenhum;
	   Transfere cada design para completed_models após a impressao"""


	while unprinted_designs:
		current_design = unprinted_designs.pop()

		#simula a criação de uma impressao 3d a partir do design
		print("Printing model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Mostra todos os modelos impressos"""
	print("\nThe fallowing models have been printed:")
	for completed_model in completed_models:
		print(completed_model)
