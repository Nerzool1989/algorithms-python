#1
a = [0]*8
for i in range(2,1000000):
    for j in range(2,10):
        if i%j == 0:
            a[j-2] += 1
print(a)

#2
from random import random
num = 10
arr = [0] * num
even = []
for i in range(num):
    arr[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
print(arr)
print('Индексы четных элементов: ', even)

#3
from random import random
num = 10
arr = [0]*num
for i in range(num):
    arr[i] = int(random()*100)
    print(arr[i],end=' ')
minimal = min(arr)
maximal = max(arr)
imn = arr.index(minimal)
imx = arr.index(maximal)
arr[imn],arr[imx] = arr[imx],arr[imn]

#4
from random import random
num = 10
arr = [0]*num
for i in range(num):
    arr[i] = int(random()*100)
    print(arr[i],end=' ')

num = arr[0]
max_frq = 1
for i in range(N-1):
    frq = 1
    for k in range(i+1,N):
        if arr[i] == arr[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]
 
if max_frq > 1:
    print(max_frq, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')

#5
from random import random
N = 15
arr = []
for i in range(N):
        arr.append(int(random() * 100) - 50)
print(arr)
 
i = 0
index = -1
while i < N:
        if arr[i] < 0 and index == -1:
                index = i
        elif arr[i] < 0 and arr[i] > arr[index]:
                index = i
        i += 1
 
print(index+1,':', arr[index])

#5 (По другому) В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# arr = [10, -3, 0, 200, 400, 0, -10]
# c = 0
# d = 0

# for i in arr:
#     if i < 0:
#         c = i
#     if d > c:
#         d = c
# print(d)
# print(arr.index(d))

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
# Сами минимальный и максимальный элементы в сумму не включать.

# найти миин и его позицию
# найти макч и его позицию
# взять сумму от и до
# from random import random

# N = 10
# a = [0]*N
# print(a)
# for i in range(N):
#     a[i] = int(random()*50)
# print(a)

# minN = a.index(min(a))
# maxN = a.index(max(a))
# print(minN, maxN)
# if maxN < minN:
#     arrN = a[(maxN+1):(minN)]
#     print(arrN)
#     summ = sum(arrN)
# else:
#     arrN = a[minN+1:maxN]
#     summ = sum(arrN)
# print(summ)

# 7. В одномерном массиве целых чисел определить два наименьших элемента. 
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# arr7 = [10, 20, 23, 5, -6, 0, -5]

# arr7copy = arr7.copy()
# print(arr7copy)
# i = 0
# minlist = []
# while i < 2:
#     minlist.append(min(arr7copy))
#     arr7copy.remove(min(arr7copy))
#     i += 1

# print(minlist)

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. 
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
M = 5
N = 4
a = []
for i in range(N):
    b = []
    s = 0
    print("%d-я строка:" % i)
    for j in range(M-1):
        n = int(input())
        s += n
        b.append(n)
    b.append(s)
    a.append(b)
 
for i in a:
    print(i)

# 9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import random
M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random()*200)
        b.append(n)
        print('%4d' % n,end='')
    a.append(b)
    print()
 
mx = -1
for j in range(M):
    mn = 200
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print("Максимальный среди минимальных: ", mx)

        
