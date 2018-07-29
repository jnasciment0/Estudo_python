file = 'alice.txt'
file_path = '/home/jasson/Documentos/Estudo/Estudo_python/capitulo_10/python_work/text_files/'+file

try:
  with open(file_path) as f_obj:
    contents = f_obj.read()
except FileNotFoundError:
  msg = "Sorry, the file " + file+ " does not exist"
  print(msg)
