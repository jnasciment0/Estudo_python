filename  = '/home/jasson/Documentos/Estudo/Estudo_python/capitulo_10/python_work/text_files/guest.txt'

with open(filename, 'w') as file_object:
  print("#######--Lista de convidado--#######")
  opcao = input("a) Adicionar convidado\nb)Sair \n")
  nome_convidado =''

  while opcao != 'b':
    if opcao == 'a':
      nome_convidado = input("Informe o nome do convidado (a): ")
      file_object.write( nome_convidado.title()+ '\n')
      opcao = input("a) Adicionar convidado\nb)Sair \n")
    else:
      exit()
