prompt = "\nTell me something, and i will repate it backu to you: "
prompt += "\nEnter 'quit' to end the program. "
active = True

message = ""

while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)
