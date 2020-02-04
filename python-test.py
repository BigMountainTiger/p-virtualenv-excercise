from modules.first_module import firstObject, set_a_number, get_a_number, a_number, ANumber
from modules.second_module import another_reference, aInt
from modules.third_module import v, print_v
import platform  

print(firstObject.name + ' - ' + str(firstObject.age))
print(firstObject is another_reference)

print(aInt)

def aMethod():
  # global aInt
  aInt = 2
  print(aInt)

aMethod()

print(aInt)

print('New test ...')

a_number = ANumber(200)
set_a_number(100)

print(get_a_number().number)
print(a_number.number)

print('Another test .....')

class A:
  def __init__(self, text):
    self.text = text

  def print_text(self):
    print(self.text)

v1 = A('V1')
v2 = v1

v2.print_text()

print(hex(id(v1)))
print(hex(id(v2)))

v2 = A('V2')

v2.print_text()

print(hex(id(v1)))
print(hex(id(v2)))

print('Third module test .....')

print(hex(id(v)))
print_v()

v = 100
print(hex(id(100)))
print(hex(id(v)))

print_v()

print('Which platform .......')
print(platform.system() + ' - ' + platform.python_implementation())