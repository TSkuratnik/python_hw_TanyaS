my_data = []
name_list = set()
price_list = set()
quantity_list = set()
unit_list = set()

my_dict = {
    'название': name_list,
    'цена': price_list,
    'количество': quantity_list,
    'ед': unit_list
}
goods_q = int(input('Введите количество товаров, которое хотите ввести: '))
for i in range(goods_q):
    name = input(f'Введите название {i+1} товара: ')
    price = int(input(f'Введите цену {i+1} товара: '))
    quantity = int(input(f'Введите количество {i+1} товара: '))
    unit = input(f'Введите единицу измерения {i+1} товара: ')
    my_data.append((i + 1, {
            'название': name,
            'цена': price,
            'количество': quantity,
            'ед': unit
        }))
    name_list.add(name)
    price_list.add(price)
    quantity_list.add(quantity)
    unit_list.add(unit)

name_list = list(name_list)
price_list = list(name_list)
quantity_list = list(name_list)
unit_list = list(name_list)
print(type(unit_list))

print(my_data)
print(my_dict)