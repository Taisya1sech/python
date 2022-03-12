class Warehouse():

    def __init__(self, ShippingWarehouseAdress)
        self.ShippingWarehouseAdress = ShippingWarehouseAdress
        self.items = {'Адрес склада-отправителя'}

    def income(self):
        try:
            self.shipping_warehouse_adress = input(f'Введите адрес склада-отправителя')
            item = {'склад-отправитель': shipping_warehouse_adress}
            self.items.update(item)
            print(self.items)
        except ValueError:
        print('Недопустимое значение!')

    def __init__(self, receiving_warehouse_adress)
        self.receiving_warehouse_adress = receiving_warehouse_adress
        self.items = {'Адрес склада-получателя'}


    def income(self):
        try:
            self.receiving_warehouse_adress = input(f'Введите адрес склада-получателя')
            item = {'Склад-получатель': receiving_warehouse_adress}
            self.items.update(item)
            print(self.items)
        except ValueError:
        print('Недопустимое значение!')

    def __init__(self, company_department_adress)
        self.company_department_adress = company_department_adress
        self.items = {'Адрес подразделения компании'}


    def income(self):
        try:
            self.shipping_warehouse_adress = input(f'Введите адрес подразделения компании')
            item = {'подразделение компании': company_department_adress}
            self.items.update(item)
            print(self.items)
        except ValueError:
        print('Недопустимое значение!')

class OfficeEquipment(Warehouse):

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


p = Printer('HP Inc', 'HP LaserJet Pro', 11000, 150)
s = Scanner('Epson', 'Epson WorkForce DS-1630', 24000, 100)
x = Xerox('Xerox Corporation', 'WorkCentre 5225 ', 158000, 15)
p.income()
s.income()
x.income()

