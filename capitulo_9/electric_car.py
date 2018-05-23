class Car():
  """Uma Tentativa simples de representar um carro"""

  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

  def get_descriptive_name(self):
    
    long_name = str(self.year) + ' ' + self.make + ' ' + self.model
    return long_name.title();

  def read_odometer(self):
    print("This car has " + str(self.odometer_reading) + " miles on it.")

  def update_odometer(self, mileage):
    
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back an odometer!")

  def  increment_odometer(self, miles):
    self.odometer_reading += miles

class Battery():
  """uma tentativa simples de modela uma bateria para um carro eletrico"""
  def __init__(self, battery_size =85):
    """Inicialza os atributos da baterias"""
    self.battery_size = battery_size

  def describe_battery(self):
    """Exebi uma frase que descreve a capacidade da bateria"""
    print("This car has a " + str(self.battery_size) + "-kwh battery.")

  def get_range(self):
    """Exebi uma frase sobre a distancia que o carro é capaz de percorre com essa bateria"""
    if self.battery_size == 70:
      range = 240
    elif self.battery_size == 85:
      range = 270
    message = "This car can go approximately " + str(range)
    message += " miles on a full charge."
    print(message)

class ElectriCar(Car):
  """Representa aspectos de um carro especificos de veiculos eletricos"""
  def __init__(self, make, model,year):
    """
    Iniciando atributos do pai.
    Em seguida, inicializa os atributos especificos de um carro eletrico
    """
    super().__init__(make, model, year)
    self.battery = Battery()
    
  def fill_gas_tank():
    """Carros eletricos não tem tanques de gasolina"""
    print("This car doesn't nees a gas tank!")

my_tesla = ElectriCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()