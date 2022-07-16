# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

array = [random.randint(-7, 12) for _ in range(30)]


arr_below =[]

for item in array:
    if item < 0:
        arr_below.append(item)
        max = arr_below[0]
        for i in arr_below:
            if i > max:
                max = i

print(f'1) Из массива {array} отберем отрицательные числа: {arr_below}')
print(f'2) Найдем максальное число из отрицательных:{max}')