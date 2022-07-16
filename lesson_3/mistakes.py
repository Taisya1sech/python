#1
a = 2
b = 99
c = 1

b = b + c

data = list(range(a, b, c))
print(data)

data_2 = []
data_3 = []
data_4 = []
data_5 = []
data_6 = []
data_7 = []
data_8 = []
data_9 = []

for item in data:
    if (item % 2 == 0):
        data_2.append(item)
        number_of_elements_2 = len(data_2)
    if (item % 3 == 0):
        data_3.append(item)
        number_of_elements_3 = len(data_3)
    if (item % 4 == 0):
        data_4.append(item)
        number_of_elements_4 = len(data_4)
    if (item % 5 ==0):
        data_5.append(item)
        number_of_elements_5 = len(data_5)
    if (item % 6 ==0):
        data_6.append(item)
        number_of_elements_6 = len(data_6)
    if (item % 7 ==0):
        data_7.append(item)
        number_of_elements_7 = len(data_7)
    if (item % 8 ==0):
        data_8.append(item)
        number_of_elements_8 = len(data_8)
    if (item % 9 ==0):
        data_9.append(item)
        number_of_elements_9 = len(data_9)


print(f'Для числа 2 кратны - {len(data_2)}')
print(number_of_elements_3)
print(number_of_elements_4)
print(number_of_elements_5)
print(number_of_elements_6)
print(number_of_elements_7)
print(number_of_elements_8)
print(number_of_elements_9)


#6
import random

r = [15, 25, 14, 14, 24, 20, 15, 21, 16, 22, 13, 22]
print(f'Исходный массив: {r}')

max = r[0]
min = r[0]

for i in r:
    if i > max:
        max = i
    elif i < min:
        min = i


max_index = r.index(max)
r.pop(max_index)
min_index = r.index(min)
r.pop(min_index)

print(f'Массив после удаления максимального и минимального элемента: {r}')
a = sum(r)
print(f'Сумма чисел между максимальным и минимальным элементом исходного массива: {a}')


#7
import random

r = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {r}')

min_index_1 = 0
min_index_2 = 1

for i in r:
    if r[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = r.index(i)
    elif r[min_index_2] > i:
        min_index_2 = r.index(i)

print(f'Два наименьших элемента: {r[min_index_1]} и {r[min_index_2]}')

'''Второй способ через сортировку списка'''

sort_list = []
sort_list.extend(r)
sort_list.sort()

print(
    f'Два наименьших элемента (второй способ): {sort_list[0]} и {sort_list[1]}'
    )