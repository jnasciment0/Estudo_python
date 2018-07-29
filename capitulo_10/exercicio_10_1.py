file_path = '/home/jasson/Documentos/Estudo/Estudo_python/capitulo_10/python_work/text_files/learning_python.txt';

with open (file_path) as dados:
  files = dados.readline()

leitura = ' '
for dado in files:
  leitura += dado

print(leitura[:52] + "...")
print(len(leitura));


# print(leitura)
  # print(files)