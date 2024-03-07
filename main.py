import math
import random

a = 1
b = 1
print(a + b)
print(1 + 1)
print(-1)
print(0)
print(1)  # int
print(1.1)  # float
print("1+1: ", 1 + 1)
print(2 - 1, "2-1")
print(2 * 1, "2*1")
print(2 / 1, "2/1")  # << float로 바꾼다!
print(2 % 1, "2%1")
print(math.sqrt(4))
print(math.pow(4, 2))
print(random.random())

print('Hello world')
print("Hello world")
print('''wow
hello''')

print("""wow
good""")

print("'1' + '1'", '1' + '1') # 11
print('hello' * 5)
print(len('hello' * 5))
print('Hello world'.replace('world', 'universe'))

students = ["egoing", "sori", "maru"]
grades = [2, 1, 4]

print(students)
print(grades)
print(len(students))
print(len(grades))

print(min(grades))
print(max(grades))

import statistics
print(statistics.mean(grades))

import random
print(random.choice(students))
