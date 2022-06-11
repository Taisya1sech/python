# Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input("Введите цело число a: "))
b = int(input("Введите цело число b: "))
c = int(input("Введите цело число c: "))

medium = a

if a < b:
    if b < c:
        medium = b
    else:
        if c > a:
            medium = c
        else:
            medium = a
else:
    if c < b:
        medium = b
    else:
        if c > a:
            medium = a
        else:
            medium = c


print(f"Среднее(больше одного, но меньше другого): {medium}")

