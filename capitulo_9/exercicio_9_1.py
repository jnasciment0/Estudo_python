class Restaurant():

  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name;
    self.cuisine_type = cuisine_type;

  def describe_restaurant(self):
    print ("O  " + self.restaurant_name.title() + " é um excelente restaurante.");
    print ("Na  cozinha do  nosso restaurante servimos " + self.cuisine_type.title() + "!");

  def open_restaurant(self):
    print("Seja Bem vindo o restaurete, estamo aberto! \n");


restaurente = Restaurant("cabeça de caranguejo","comida tipica paraense")

restaurente.open_restaurant();
restaurente.describe_restaurant();