class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на нуль недопустимо!")


div = DivisionByNull(40, 57)
print(DivisionByNull.divide_by_null(40, 0))
print(DivisionByNull.divide_by_null(40, 0.7))
print(div.divide_by_null(57, 0))

