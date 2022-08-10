
def max1(a, b, c):
    print(max(a, b, c))

print(max1(3, 4, 6))
#2
list1 = [8, 2, 3, 0, 7]

def numbers(list1):
    b = 0
    for i in list1:
            b += i
    print(b)
numbers(list1)
#3
list1 = [8, 2, 3, 0, 7]

def numbers(list1):
    b = 1
    for i in list1:
            b = b * i
    print(b)
numbers(list1)
#4
def string1(a):
    print(a[::-1])
print(string1("1234abcd"))
#5
numbers = list(map(int, input().split()))
common_list = []
final_list = []

for i in numbers:
    common_list.append(i)
    if common_list.count(i) <= 1:
        final_list.append(i)
print(final_list)
#6
number = int(input())

def qator(number):
    string = '12345'
    for x in string:
        if int(x) == number:
            print("yes")
qator(number)
#7
def kvadrat():
    for i in range(1, 30):
        print(i ** 2)
kvadrat()
#8

import math

list1 = list(map(int, input().split()))
def kvadratildiz(list1):
    for x in list1:
        print(math.sqrt(x))
kvadratildiz(list1)
#9
questions = ['Name', 'Age', 'Score', 'Smth about you']
info = {}
def usersinfo(questions):
    for question in questions:
        print(question, ' ')
        answer = input()
        info[question] = answer
    for key, value in info.items():
        print(key, '-', value, '\n')
usersinfo(questions)
#11
a = int(input())
b = int(input())
def fun(a, b):
    print(a + b)
    print(a + 5)
    print(a + 5)
print(fun(a, b))
#12
def check(a):
    if a % 2 == 0:
        print(a, 'чет')
    else:
        print('нечет')
a = int(input())
print(check(a))
#10 lambda otmadik
#13 factorial ne zn
#14 ne zn
#15 lambda
# 16
def kub(a):
    print(a ** 3)
a = int(input())
print(kub(a))
