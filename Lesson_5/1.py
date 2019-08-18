import collections
count = int(input('Введите кол-во компаний: '))
comp = collections.defaultdict(list)
for i in range(count):
 name = input(f'Введите имя {i + 1} компании: ')
 profit = [(int(input(f'Введите прибыль за {j+1} квартал: '))) for j in range(4)]
 comp[name] = sum(profit)
avg_prof = sum(comp.values()) / count
print(f'Средняя прибыль {avg_prof}')
for i in comp:
 if comp[i] < avg_prof:
 print(f'Компания "{i}" имеет прибыль НИЖЕ средней: ({comp[i]})')
 elif comp[i] > avg_prof:
 print(f'Компания "{i}" имеет прибыль ВЫШЕ средней: ({comp[i]})')