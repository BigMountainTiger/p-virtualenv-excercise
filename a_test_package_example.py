import sys
from test_package.module1 import module1
from test_package.module2 import module2

print(module1['name'])
print(module2['name'])

print()
print('sys.modules:')

for m in sys.modules:
  print(m)

# print(sys.modules['test_package.module1'])
# print(sys.modules['test_package.module2'])
# print(sys.modules['test_package'])