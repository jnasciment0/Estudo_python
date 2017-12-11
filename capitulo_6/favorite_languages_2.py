favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python'
}
# print("The following languages have been mentioned:")
# #usando set (conjunto)
# for language in set(favorite_languages.values()):
# 	print(language.title())



# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
# 	print(language.title())

#ordenando as keys com o sorted
# for name in sorted(favorite_languages.keys()):
# 	print(name.title() + ", thank you for taking the poll")

friends = ['phil','sarah']
#exibindo somente as key's do dicionario
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print(" Hi "+name.title() + ", I see you favorite language is " + favorite_languages[name].title() + "!")
	elif 'erin' not in favorite_languages.keys():
		print("Erin, please take our poll!")

# for name , language in favorite_languages.items():
# 	print(name.title() + "'s favorite language is " + language.title())