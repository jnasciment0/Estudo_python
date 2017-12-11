rios ={
	'nilo':'egito',
	'rio tocantins':'goias',
	'rio amazonas':'amazonia',
	'são francisco':'minas gerais'
}

for k, v in rios.items():
	print("O " + k.title() + " corre pelo(a) " + v.title())

for name in rios.keys():
	print("\nRio " + name)
