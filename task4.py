a = int(input("Введите любое целое поожительное число"))
max_num = 0
while a > 10:
    if a % 10 > max_num:
        max_num = a % 10
        if max_num == 9:
            break
    a = a // 10

print(f"Наибольшая цифра числа: {max_num}")