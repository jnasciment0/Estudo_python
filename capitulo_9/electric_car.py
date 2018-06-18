"""Um conjunto de classes que pode ser usado para representar carros Eletricos"""
from car import Car

class Battery():
  """uma tentativa simples de modela uma bateria para um carro eletrico"""
  def __init__(self, battery_size = 60):
    """Inicialza os atributos da baterias"""
    self.battery_size = battery_size

  def describe_battery(self):
    """Exebi uma frase que descreve a capacidade da bateria"""
    print("This car has a " + str(self.battery_size) + "-kwh battery.")

  def get_range(self):
    """Exebi uma frase sobre a distancia que o carro é capaz de percorre com essa bateria"""
    range = 0
    if self.battery_size == 70:
      range = 240
    elif self.battery_size == 85:
      range = 270
  
class ElectricCar(Car):
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