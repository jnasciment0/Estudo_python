class User():
  """Classe de usuários"""
  def __init__(self, first_name, last_name,year,nick_name):
    self.first_name = first_name;
    self.last_name = last_name;
    self.year = year;
    self.nick_name = nick_name;

  def describe_user(self):
    print("######## - Dados do Usuário - ########");
    print("Primeiro nome: " + self.first_name.title());
    print("Ultimo nome: " + self.last_name.title());
    print("Idade do jogador:  " + str(self.year));
    print("Nick name do jogador:  " + self.nick_name);

  def greet_user(self):
    print("Seja muito bem vindo jogar " + self.nick_name);
    print("O jogo ira começar em algum segundos!");

usuarios = User("jasson", "nascimento", 28, "chefao);
