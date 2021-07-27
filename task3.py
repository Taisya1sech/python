def my_func(a, b, c):
    sum_nums = a + b + c
    return sum_nums - min((a, b, c))


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
x = my_func(a, b, c)
print(x)
