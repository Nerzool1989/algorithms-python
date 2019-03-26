# 1
# print("Чтобы выйти введите ноль")
# while True:
#         s = input("Знак (+,-,*,/): ")
#         if s == '0': break
#         if s in ('+','-','*','/'):
#                 x = float(input("x="))
#                 y = float(input("y="))
#                 if s == '+':
#                         print("%.2f" % (x+y))
#                 elif s == '-':
#                         print("%.2f" % (x-y))
#                 elif s == '*':
#                         print("%.2f" % (x*y))
#                 elif s == '/':
#                         if y != 0:
#                                 print("%.2f" % (x/y))
#                         else:
#                                 print("Делить на ноль нельзя")
#         else:           
#                 print("Неверный знак операции!")

# 2

n = int(input())
even = 0
odd = 0
while n > 0:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    n = n//10
print("четных - %d, нечетных - %d" % (even, odd))

# 3

n = input()
n[::-1]
print(n)

# 4

n = int(input())
e = 1
s = 0
for i in range(n):
    s += e
    e /= -2
print(s)

# 5

for i in range(32,128):
    print("%4d-%s" % (i,chr(i)), end='')
    if i%10 == 0:
        print()
 
print()

# 6

from random import random

n = round(random() * 100)
i = 1
print("Компьютер загадал число. Отгадайте его. У вас 10 попыток")
while i <= 10:
    u = int(input(str(i) + '-я попытка: '))
    if u > n:
        print('Много')
    elif u < n:
        print('Мало')
    else:
        print('Вы угадали с %d-й попытки' % i)
        break
    i += 1
else:
    print('Вы исчерпали 10 попыток. Было загадано', n)

# 7

n = int(input())
s = 0
for i in range(1,n+1):
    s += i
m = n * (n + 1) // 2
print(s)
print(m)

# 8

n = int(input("Сколько будет чисел? "))
d = int(input("Какую цифру считать? "))

count = 0
for i in range(1,n+1):
    m = int(input("Число " + str(i) + ": "))
    while m > 0:
        if m%10 == d:
            count += 1
        m = m // 10
 
print("Было введено %d цифр %d" % (count, d))