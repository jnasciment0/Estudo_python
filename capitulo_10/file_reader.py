file_path = '/home/jasson/Documentos/Estudo/Estudo_python/capitulo_10/python_work/text_files/pi_digits.txt';
with open(file_path) as file_object:
  lines = file_object.readlines()
  for line in lines:
    print(line.rstrip())






# with open(file_path) as file_object:
#   contents = file_object.read();
#   print(contents);