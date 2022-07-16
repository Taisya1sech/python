# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# В данном случае выбран метод быстрой сортировки
import random

r = [random.randint(7, 85) for _ in range(15)]
print(f'Исходный массив: {r}')

max = r[0]
min = r[0]

for i in r:
    if i > max:
        max = i
    elif i < min:
        min = i
min_index = r.index(min)
max_index = r.index(max)
r[min_index], r[max_index] = r[max_index], r[min_index]
print(f'Массив после того, как мы поменяли местами минимальное число с индексом {min_index} и максимальное число с индексом {max_index}: {r}')