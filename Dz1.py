# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь. 

def getNumber():
    num = input("введите трехзначное число: ")
    return calcSummary(num)

def isNotNumber(str):
    try:
        int(str)
        return False
    except:
        return True

def calcSummary(num):
    if isNotNumber(num) or len(num) != 3: 
        print("Я сказал трехзначное число")
        return getNumber()
    else:
        sum = 0
        for i in num:
            sum += int(i)
        print(sum)
        return getNumber()

# getNumber()

# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

a = 5
b = 6
print(bin(a))
print(bin(b))

resAnd = a & b
print(resAnd)

resOr = a | b
print(resOr)

resBitRight = a >> 2
print(resBitRight) 
#Предназначено для экономии памяти в формате 1 байт

# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
# print("Координаты точки A(x1;y1):")
# x1 = float(input("\tx1 = "))
# y1 = float(input("\ty1 = "))
 
# print("Координаты точки B(x2;y2):")
# x2 = float(input("\tx2 = "))
# y2 = float(input("\ty2 = "))
 
# print("Уравнение прямой, проходящей через эти точки:")
# k = (y1 - y2) / (x1 - x2)
# b = y2 - k*x2
# print(f" y = {k}*x + {b}")


# 4.	Написать программу, которая генерирует в указанных пользователем границах
# ●	случайное целое число,
# ●	случайное вещественное число,
# ●	случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random
import string
# СЛУЧАЙНЫЙ целое число
# randInt1 = int(input("введите начало диапазона: "))
# randInt2 = int(input("введите конец диапазона: "))

# print(random.randrange(randInt1, randInt2))

# СЛУЧАЙНЫЙ вещественное число
# randFl1 = float(input("введите начало диапазона: "))
# randFl2 = float(input("введите конец диапазона: "))

# print(random.uniform(randFl1, randFl2))

# СЛУЧАЙНЫЙ СИМВОЛ
# alphabet = string.ascii_letters
# randStr1 = alphabet.find(input("введите символ начала: ")) 
# randStr2 = alphabet.find(input("введите конечный символ: ")) 

# randNum = random.randrange(randStr1,randStr2)
# print(alphabet[randNum])

# 5.	Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
# alphabet = string.ascii_letters
# randPosit1 = alphabet.find(input("введите символ начала: ")) 
# randPosit2 = alphabet.find(input("введите конечный символ: ")) 
# print(randPosit1)
# print(randPosit2)
# print(len(alphabet[randPosit1: randPosit2]))

# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# alphabet = string.ascii_letters
# numUser = alphabet.find(input("Введите номер буквы в алфавите: "))
# print(numUser)

# 7.	По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. 
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

# a = int(input("Введите сторону a = "))
# b = int(input("Введите сторону b = "))
# c = int(input("Введите сторону c = "))
 
# if (a + b <= c) or (a + c <= b) or (b + c <= a):
#     print("Треугольник не существует")
# elif (a != b) and (a != c) and (b != c):
#     print("Разносторонний")
# elif a == b == c:
#     print("Равносторонний")
# else:
#     print("Равнобедренный")

# 8.	Определить, является ли год, который ввел пользователь, високосным или не високосным.

# year = int(input('Введите кол-во дней в 3х значном формате для проверки года: '))
# if(year % 366 == 0):
#     print("год високосный")
# else:
#     print("год невисокосный")

# 9.	Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# print('Введите три числа: ')
# a = int(input())
# b = int(input())
# c = int(input())
 
# if (b < a < c) or (c < a < b):
#     print('Среднее:', a)
# elif (a < b < c) or (c < b < a):
#     print('Среднее:', b)
# else:
#     print('Среднее:', c)
