class _FirstClass:
  def __init__(self, name, age):
    self.name = name
    self.age = age


firstObject = _FirstClass('Song', 20)

class ANumber:
  def __init__(self, n):
    self.number = n

a_number = ANumber(50)

def set_a_number(n):
  a_number.number = n

def get_a_number():
  return a_number

print('first_module initiated ....')