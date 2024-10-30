from modules.module_1 import count_num
from package.file_container_1.file_container_in_fc_1.file_3 import file_3

number = input("Введите число")
print(count_num(number))

from modules.module_2 import oddnum
a = 20
b = 40
print(oddnum(a,b))

from package.file_container_1.file_1 import file_1
print(file_1())

from package.file_container_1.file_2 import file_2
print(file_2())

from package.file_container_1.file_container_in_fc_1.file_3 import file_3
print(file_3())

from package.file_container_1.file_container_in_fc_1.file_4 import file_4
print(file_4())

from package.file_container_2.file_5 import file_5
print(file_5())

from package.file_container_2.file_6 import file_6
print(file_6())