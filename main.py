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


# class A:
#     def greeting(self):
#         print('안녕하세요. A입니다.')
#
#
# class B(A):
#     def greeting(self):
#         print('안녕하세요. B입니다.')
#
#
# class C(A):
#     def greeting(self):
#         print('안녕하세요. C입니다.')
#
#
# class D(B, C):
#     pass
#
# class E(C, B):
#     pass
#
#
# x = D()
# x.greeting()  # 안녕하세요. B입니다.
# print(D.mro())
#
# x2 = E()
# x2.greeting()  # 안녕하세요. C입니다.
# print(E.mro())


class Animal:
    def eat(self):
        print("Eating")


class FlyingAnimal(Animal):
    def fly(self):
        print("Flying")


class SwimmingAnimal(Animal):
    def swim(self):
        print("Swimming")


class Bird(FlyingAnimal):
    def fly(self):
        print("Flying")
    pass


class Fish(SwimmingAnimal):
    pass


class Duck(Bird, SwimmingAnimal):  # 다이아몬드 상속
    pass

duck = Duck()
duck.eat()          # Eating
duck.fly()          # Flying
duck.swim()         # Swimming