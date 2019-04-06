#Я не особо уверен что я правильно сделал, но вывод внизу
import cProfile
from random import random

def fff():
    N = 10
    a = [0]*N
    print(a)
    for i in range(N):
        a[i] = int(random()*50)
    print(a)

    minN = a.index(min(a))
    maxN = a.index(max(a))
    print(minN, maxN)
    if maxN < minN:
        arrN = a[(maxN+1):(minN)]
        print(arrN)
        summ = sum(arrN)
    else:
        arrN = a[minN+1:maxN]
        summ = sum(arrN)
    print(summ)

cProfile.run('fff()')

def get_count(items):
   return len(items)

def get_sum(items):
   sum_ = 0
   for i in items:
       sum_ += i
   return sum_

def main():
   a = [3,5,6,7]
   s = get_count(a)
   t = get_sum(a)

cProfile.run('main()')

def f(n):
    if n < 2:
        return n
    pp = 0
    p = 1
    for i in range(n - 1):
        pp, p = p, pp + p
    return p

cProfile.run('f(20)')

# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [29, 33, 31, 0, 26, 38, 33, 26, 1, 25]
# 3 5
# 26
#          43 function calls in 0.000 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 DZPYTHON.py:5(fff)
#        10    0.000    0.000    0.000    0.000 cp1251.py:18(encode)
#        10    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#         4    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#        10    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}


#          7 function calls in 0.000 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 DZPYTHON.py:27(get_count)
#         1    0.000    0.000    0.000    0.000 DZPYTHON.py:30(get_sum)
#         1    0.000    0.000    0.000    0.000 DZPYTHON.py:36(main)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#          4 function calls in 0.000 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 DZPYTHON.py:43(f)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 2 алгоритм грека Эратосфена (без я что-то затрудняюсь... (и нет времени...))
def primes(n):
    a = [0] * n 
    for i in range(n): 
        a[i] = i 
     
    a[1] = 0
     
    m = 2 
    while m < n: 
        if a[m] != 0: 
            j = m * 2 
            while j < n:
                a[j] = 0 
                j = j + m 
        m += 1
     
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
     
    del a
    return b