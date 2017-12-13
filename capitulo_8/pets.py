def describe_pet(animal_type, pet_name):
	"""Exibe informações sobre um animal de estimação"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type ='hamster',pet_name='harry')
describe_pet(animal_type ='dog',pet_name='willie')
# describe_pet('hamster','harry')
# describe_pet('dog','willie')