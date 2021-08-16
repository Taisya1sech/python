class OfficeEquipment:

    def __init__(self, supplier, model, price, quantity):
        self.supplier = supplier
        self.model = model
        self.price = price
        self.quantity = quantity
        self.items = {'Копмания-производитель': self.supplier, 'Модель устройства': self.model, 'Цена за шт': self.price, 'Количество': self.quantity}

    def income(self):
        try:
            supplier = input(f'Введите название компании-производителя: ')
            model = input(f'Введите название модели: ')
            price = int(input(f'Введите цену за шт: '))
            quantity = int(input(f'Введите количество: '))
            item = {'Компания-производитель': supplier, 'Модель устройства': model, 'Цена за шт': price, 'Количество': quantity}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('Недопустимое значение!')


class Printer(OfficeEquipment):
    pass


class Scanner(OfficeEquipment):
    pass


class Xerox(OfficeEquipment):
    pass


p = Printer('HP Inc', 'HP LaserJet Pro', '11000', '150')
s = Scanner('Epson', 'Epson WorkForce DS-1630', '24000', '100')
x = Xerox('Xerox Corporation', 'WorkCentre 5225 ', '158000', '15')
p.income()
s.income()
x.income()
