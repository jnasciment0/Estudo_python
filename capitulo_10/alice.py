file = 'alice.txt'
file_path = '/home/jasson/Documentos/Estudo/Estudo_python/capitulo_10/python_work/text_files/'+file

try:
  with open(file_path) as f_obj:
    contents = f_obj.read()
except FloatingPointError:
  msg = "Sorry, the file " + file_path + " does not exist!"
else:
  #Conta o numero aproximadp de palavras no arquivo
  words = contents.split()
  num_words = len(words)
  print("The file "+ file+ " has about " + str(num_words) + " words.")



# try:
#   with open(file_path) as f_obj:
#     contents = f_obj.read()
# except FileNotFoundError:
#   msg = "Sorry, the file " + file+ " does not exist"
#   print(msg)
