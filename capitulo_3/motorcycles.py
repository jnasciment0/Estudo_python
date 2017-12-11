motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'

motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

#removendo um item de acordo com o valor
# motorcycles.remove('ducati')
# print(motorcycles)


#removendo item de qualquer posição
# first_owned = motorcycles.pop(0)
# print("The first motorcycle I owned was a " + first_owned.title() + ".")


# last_owned = motorcycles.pop()
# print(last_owned)
# print(motorcycles)
# print("The last motorcycle I owned was a " + last_owned.title() + ".")


#usando o metodo pop
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

#removendo um elemento da lista
# del motorcycles[0]
# print(motorcycles)

#inserindo elemento na lista (posição 0)
# motorcycles.insert(0,'ducati')
# print(motorcycles)
#inserindo um elemento na lista
# motorcycles.append('ducati')
# print(motorcycles)
#alterando um elemento da lista
# motorcycles[0] ='ducati'


# motorcycles = []

# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# motorcycles.append('ducati')

# print(motorcycles)