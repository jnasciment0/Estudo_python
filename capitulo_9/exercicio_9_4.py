class Restaurant():

  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name;
    self.cuisine_type = cuisine_type;
    self.number_server = 0

  def describe_restaurant(self):
    print ("O  " + self.restaurant_name.title() + " é um excelente restaurante.");
    print ("Na  cozinha do  nosso restaurante servimos " + self.cuisine_type.title() + "!");
    

  def open_restaurant(self):
    print("Seja Bem vindo o restaurete, estamo aberto! \n");
  
  def read_numer_server(self):
  	print("Iniciamos os atendimentos....")
  	print("Quantidade de cliente atendidos é: "+str(self.number_server))

  def set_number_served(self,number_server):
  	self.number_server = number_server
  	# print("Quantidade de cliente atendidos é: " + str(self.number_server))

  def increment_number_served(self,number_server):
  	self.number_server +=number_server

restaurente = Restaurant("cabeça de caranguejo","comida tipica paraense")

restaurente.open_restaurant();
restaurente.describe_restaurant();
restaurente.set_number_served(5);
restaurente.increment_number_served(101)
restaurente.increment_number_served(1000)

restaurente.read_numer_server();

# restaurente.increment_number_served(10);