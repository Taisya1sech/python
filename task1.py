def div_nums(a, b):
    if b == 0:
        return "You can not devide to 0!"
    else:
        return a / b

a = float(input("a: "))
b = float(input("b: "))
print(div_nums(a, b))
