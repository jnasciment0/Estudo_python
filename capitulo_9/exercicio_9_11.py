class User():
  """Classe de usuários"""
  def __init__(self, first_name, last_name,year,nick_name):
    self.first_name = first_name;
    self.last_name = last_name;
    self.year = year;
    self.nick_name = nick_name;
    self.count_login = 0


  def describe_user(self):
    print("\n######## - Dados do Usuário - ########");
    print("Primeiro nome: " + self.first_name.title());
    print("Nick name do jogador:  " + self.nick_name + "\n");

  def greet_user(self):
    print("Seja muito bem vindo jogar " + self.nick_name);
    print("O jogo ira começar em algum segundos!");

  def login_attempst(self):
    tentativa_de_login = 'Nick: ' + self.nick_name + '\nTentativa de logar no game: ' + str(self.count_login);
    return tentativa_de_login

  def increment_login_attempts(self):
    self.count_login +=  1

  def reset_login_attempts(self):
     self.count_login = 0
     print("Zerando as tentivas de logar")

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
     
   


# usuarios.greet_user();


# usuarios.show_privileges();
# print(usuarios.login_attempst());
# usuarios.increment_login_attempts();
# print(usuarios.login_attempst());
# usuarios.increment_login_attempts();
# print(usuarios.login_attempst());
# usuarios.reset_login_attempts();
# print(usuarios.login_attempst());

# usuarios = User("jasson", "nascimento", 28, "chefao");
# usuarios.greet_user();
# usuarios.describe_user();
# print(usuarios.login_attempst());
# usuarios.increment_login_attempts();
# usuarios.increment_login_attempts();
# usuarios.increment_login_attempts();
# usuarios.increment_login_attempts();
# # usuarios.increment_login_attempts();
# print(usuarios.login_attempst());
# usuarios.reset_login_attempts();
# print(usuarios.login_attempst());