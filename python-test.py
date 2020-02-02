from modules.first_module import firstObject, set_a_number, get_a_number, a_number, ANumber
from modules.second_module import another_reference, aInt

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