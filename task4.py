def get_pow(x, y):
    if x < 0:
        return 'X must be greater than 0'
    if y > 0:
        return 'Y must be less than 0'
    z = 1
    for i in range(y * -1):
        z *= x
    return 1 / z


x = float(input("Please enter a positive number (x): "))
y = float(input("Please enter a negative integer (y): "))
print(get_pow(x, y))
