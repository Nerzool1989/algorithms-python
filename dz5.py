# 1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) 
# для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

numbFabr = 4
nameFabr = dict(f1 = 10, f2 = 12, f3 = 9, f4 = 16)

fabrVal = []
for i in nameFabr:
    fabrVal.append(nameFabr[i])

midlFabr = sum(fabrVal)/len(fabrVal)

for i in nameFabr:
    if nameFabr[i] < midlFabr:
        print(f'Fabric below middle {i}')
    else:
        print(f'Fabric under middle {i}')
