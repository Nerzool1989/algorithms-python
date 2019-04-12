import sys

# Прога 1
import string
alphabet = string.ascii_letters
randPosit1 = alphabet.find('A') 
randPosit2 = alphabet.find('F') 
print(randPosit1)
print(randPosit2)
print(len(alphabet[randPosit1: randPosit2]))

print(f'кол-во памяти первой программы: {sys.getsizeof(alphabet) + sys.getsizeof(randPosit1) + sys.getsizeof(randPosit2)}')



# Прога 2
print("Подсчет затраченной памяти второй проги")
numbFabr = 4
nameFabr = dict(f1 = 10, f2 = 12, f3 = 9, f4 = 16)
print(nameFabr)

fabrVal = []
for i in nameFabr:
    fabrVal.append(nameFabr[i])

midlFabr = sum(fabrVal)/len(fabrVal)

for i in nameFabr:
    if nameFabr[i] < midlFabr:
        print(f'Fabric below middle {i}')
    else:
        print(f'Fabric under middle {i}')



print(f'затрачено памяти: {sys.getsizeof(numbFabr) + sys.getrefcount(nameFabr) + sys.getrefcount(fabrVal) + sys.getrefcount(midlFabr)}')
# Python 3.7.3, разрядность системы 64 бита
# По итогам: 1 программа весомей из-за использования алфавита из подключаемой библиотеки
