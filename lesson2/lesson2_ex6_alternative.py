my_data = []
name_list = []
price_list = []
quantity_list = []
unit_list = []

my_dict = {
    'название': name_list,
    'цена': price_list,
    'количество': quantity_list,
    'ед': unit_list
}

goods_q = int(input('Введите количество товаров, которое хотите ввести: '))
for i in range(goods_q):
    name = input(f'введите название {i+1} товара: ')
    price = int(input(f'введите цену {i+1} товара: '))
    quantity = int(input(f'введите количество {i+1} товара: '))
    unit = input(f'введите единицу измерения {i+1} товара: ')
    my_data.append((i + 1, {
            'название': name,
            'цена': price,
            'количество': quantity,
            'ед': unit
        }))
    name_list.append(name)
    price_list.append(price)
    quantity_list.append(quantity)
    unit_list.append(unit)

name_list = list(set(name_list))
price_list = list(set(name_list))
quantity_list = list(set(name_list))
unit_list = list(set(name_list))

print(my_data)
print(my_dict)