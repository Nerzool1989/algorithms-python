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
