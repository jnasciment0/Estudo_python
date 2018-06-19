from exercicio_9_12 import User

class Privileges():
  """docstring for ClassName"""
  def __init__(self):
    
    self.privileges = ["can add post","can delet post", "can ban user"]

  def show_privileges(self):
    for lista_de_privilegios in self.privileges:
        print("-" + lista_de_privilegios.title() )
    

class Admin(User):
  """docstring for Admin"""
  def __init__(self, first_name, last_name,year,nick_name):
    super().__init__(first_name, last_name,year,nick_name)
    self.teste = Privileges()

  def permisao_de_administrador(self):
    
    if self.nick_name == "admin":
      print("Lisda de privilegios do adminitrativos:")
      self.teste.show_privileges()
    else:
      print("Usuario normal")
     