file = 'apache2_access.log'
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
  #
  campos = [] ;
  campos = contents.split(" ");
  i = 0
while i < len(campos):
        print (campos[i])
        i = i + 1

  # for indice, valor in enumerate(campos):
  #   print(str(indice) + ' '+ valor)
  # for x in campos:
  #   print(x[1]);
  #   # n_pos = n_list.index(n_min) # pega a posição do valor n_min
    # n_list = [ int(x) for x in contents.split() ]




  # for (int i = 0; i < linha.length(); i++){ System.out.println("Indice "+ i +" " +campos[i]);}



# n_list = [ int(x) for x in numbers.split() ]

# n_min = min(n_list)
# n_pos = n_list.index(n_min) # pega a posição do valor n_minn