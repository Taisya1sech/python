class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.y = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма y1 и y2 равна')
        return f'y = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение c1 и c2 равно')
        return f'y = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'y = {self.a} + {self.b} * i'


y_1 = ComplexNumber(7, -4)
y_2 = ComplexNumber(2, 5)
print(y_1)
print(y_1 + y_2)
print(y_1 * y_2)

