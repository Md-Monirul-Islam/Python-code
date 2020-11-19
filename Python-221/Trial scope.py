print(1e10)
print('%.2f'%12.34556)
print('%e'%12.3456)
name = 'MunNa'
print(len(name))
print(name.lower())
print(name)
N = name.lower()
print(N)
a = 0
def my_function():
    global a
    a = 3
    print(a)
my_function()
print(a)

Lower,UPPER,CAPITAL = 1,2,3
name = 'munna'
print_style = UPPER
if print_style == Lower:
    print(name.lower())
if print_style == UPPER:
    print(name.upper())
if print_style == CAPITAL:
    print(name.capitalize())

import math
import re
import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(math.pi)
print(re.IGNORECASE)

my_list = [1,2,3]
my_list[0]=5
print(my_list)

course_code = 1202
DEPARTMENT_NAMES = {
    "CSE" : "Computer Science and Engineering",
    "MAM" : "Mathematics and Appplied Mathematics",
    "STA" : "Statical Science",
}

if course_code in DEPARTMENT_NAMES:
    print("Department: %s" % DEPARTMENT_NAMES[course_code])
else:
    print("Unknown course code: %s" % course_code)

numbers = [1, 2, 3, 4, 5]
numbers.append(5)
numbers.count(5)
numbers.extend([56, 2, 12])
print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] * 3)


even_numbers = {2, 4, 6, 8, 10}
big_numbers = {6, 7, 8, 9, 10}
print(big_numbers - even_numbers)
print(big_numbers | even_numbers)

marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }
personal_details = {
    "name": "Jane Doe",
    "age": 38, # trailing comma is legal
}
print(marbles["green"])
print(personal_details["name"])
marbles["red"] += 3
print(marbles["Red"])




