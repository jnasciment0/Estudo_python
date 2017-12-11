favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python'
}

friends = {'phil','sarah'
#exibindo somente as key's do dicionario
for name in favorite_languages.keys():
	print(name.title())
	# if name in friends:
	if friends not in favorite_languages:
		print(" Hi "+name.title() + ", I see you favorite language is " + favorite_languages[name].title() + "!")
	elif 'erin' not in favorite_languages.keys():
		print("Erin, please take our poll!")
