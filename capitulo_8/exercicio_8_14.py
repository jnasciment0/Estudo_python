def make_car(marca,fabricante,**outras_inf):
	
	car={}
	car['marca_car']= marca
	car['fabricante_car']=fabricante
	
	for key, value in outras_inf.items():
		car[key]= value
	return car

# carro = make_car('Gol','volkswarg',cor='cinza',pelicu='g5',geracao='g7')
carro = make_car('subaru','outback',color='blue',tow_packge=True)

print(carro)