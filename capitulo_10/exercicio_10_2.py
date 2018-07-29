file_path = '/home/jasson/Documentos/Estudo/Estudo_python/capitulo_10/python_work/text_files/learning_python.txt';

with open (file_path) as dados:
  files = dados.readline()

print(files.replace('python','Jasson'))