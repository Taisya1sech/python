a = int(input("Выручка: "))
b = int(input("Издержки: "))

if b > a:
    print("Убыток")
elif a > b:
    print("Прибыль")
    c = round((a - b) / a, 2)
    print(f"Рентабельность: {c}")
    d = int(input("Количество штатных сотрудников: "))
    d = round((a-b) / d, 2)
    print(f"Прибыль фирмы в расчете на одного сотрудника: {d}")
elif a == b:
    print("Финансовый результат = 0")