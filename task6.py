products = [
    (1, {'name': 'book', 'price': '1500', 'amount': '20', 'units': 'piece'}),
    (2, {'name': 'pen', 'price': '50', 'amount': '100', 'units': 'piece'}),
    (3, {'name': 'eraser', 'price': '37', 'amount': '75', 'units': 'piece'})
]

result_list = {}
for numb, prod_dict in products:
    for key, value in prod_dict.items():
        if not result_list.get(key):
            result_list[key] = [value]
        else:
            result_list[key].append(value)

print(result_list)
