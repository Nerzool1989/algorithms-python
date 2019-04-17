#ЗАДАЧА 1
from random import random
import numpy as np
# randomArr = np.random.randint(-100, 101, 50)
# def (randomArr):
# n = 1
# while n < len(li):
#      for i in range(len(li)-n):
#           if li[i] < li[i+1]:
#                li[i],li[i+1] = li[i+1],li[i]
#      n += 1
# print(li) 

#Задача 2
randomArrPrime = np.random.randint(0, 50, 50) #оказывает он блин class array возвращает
ar = list(randomArrPrime)
print(type(ar))

def merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(list):
  if len(list) < 2:
      return list
  middle = len(list) // 2
  left = mergesort(list[:middle])
  right = mergesort(list[middle:])
  return merge(left, right)

# mergesort(randomArrPrime)
# print(randomArrPrime)

list1 = [20, 100, 10, 11, 12, 15, 30]
print(type(list1))
print(mergesort(list1))
print(mergesort(ar))
