class Car():
  """Uma Tentativa simples de representar um carro"""
  def __init__(self, make, model, year):
    """Inicializa os atributos que descrevem um carro."""
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 5

  def get_descriptive_name(self):
    """Devolver um nome descritivo, formatado de modeo elegante"""
    long_name = str(self.year) + ' ' + self.make + ' ' + self.model
    return long_name.title();

  def read_odometer(self):
    """Exibe uma frase que mostra a milhagem do carro."""
    print("This car has " + str(self.odometer_reading) + " miles on it.")

  def update_odometer(self, mileage):
    """Define o valor de leitura do hodômetro com o  valor especificado
          Rejeita a alteração se for tentativa de definir um valor menor para  hodômetro
    """
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back an odometer!")

  def  increment_odometer(self, miles):
    """Soma a quantidade especifica ao valor de leitura do hodômetro"""
    self.odometer_reading += miles

my_used_car = Car('subaru', 'outbak', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
# my_new_car = Car('audi','a4',2016);
# print(my_new_car.get_descriptive_name( ));
# my_new_car.odometer_reading = 23;
# my_new_car.update_odometer(1);
# my_new_car.read_odometer();