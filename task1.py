import sys

if len(sys.argv) < 4:
    raise ValueError(f"Введите все данные (выработка, ставка, премия)!")
else:
    a = float(sys.argv[1])
    b = flaot(sys.argv[2])
    c = float(sys.argv[3])
    result = a * b + c
    print(result)



