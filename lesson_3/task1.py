# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.


result = {}
for k in range(2, 10):
    result[k] = []
    for n in range(2, 100):
        if n % k == 0:
            result[k].append(k)
            z = len(result[k])
    print(f'Для числа {k} кратны {z} чисел в диапозоне от 2 до 99')
