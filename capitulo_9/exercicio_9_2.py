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
restaurente2 = Restaurant("Tta dora","comidas tipicas")
restaurente3 = Restaurant("roxy bar","comida de outro mundo")

restaurente2
restaurente.open_restaurant();
restaurente.describe_restaurant();

restaurente2.open_restaurant();
restaurente2.describe_restaurant();

restaurente3.open_restaurant();
restaurente3.describe_restaurant();
