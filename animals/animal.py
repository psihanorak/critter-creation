from datetime import date

class Animal:
  def __init__(self, name, species, food, chip_num):
    self.name = name
    self.species = species
    self.food = food
    self.date_added = date.today()
    self._chip_num = chip_num
