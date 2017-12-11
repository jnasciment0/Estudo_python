lugares = ['USA', 'POLO NORTE', 'BARCELONA', 'JAPAO', 'NOVA ZELANDIA']
print('Lista original: ' + str(lugares))

#usando o sorted
print("Lista em ordem alfabetica: " + str(sorted(lugares)))
print("Lista em ordem alfabetica Inversa: " + str(sorted(lugares, reverse = True)))

#usando o reverse
print("\nLista original sem o reverse: " + str(lugares))
lugares.reverse()
print("Mudando a ordem com o reverse: " + str(lugares))
lugares.reverse()
print("Mudando a ordem com o reverse pra voltar ao original: " + str(lugares) + "\n")

#usando o sort
lugares = ['USA', 'POLO NORTE', 'BARCELONA', 'JAPAO', 'NOVA ZELANDIA']
print('Lista original: ' + str(lugares))
lugares.sort()
print('Lista em ordem alfabetica com sort: ' + str(lugares))
lugares.sort(reverse = True)
print('Lista em ordem alfabetica com sort inversa: ' + str(lugares))
