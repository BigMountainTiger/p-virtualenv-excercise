from modules.first_module import firstObject
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