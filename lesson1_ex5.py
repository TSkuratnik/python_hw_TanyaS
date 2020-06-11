revenue = int(input('Введите выручку Вашей фирмы: '))
cost = int(input('Введите издержки Вашей фирмы: '))
profit = revenue - cost
if profit > 0:
    print('Поздравляем, Ваша фирма  работает с прибылью!')
    profitability = profit / revenue
    print('Рентабельность выручки: ', profitability)
    workers_q = int(input('Введите количество сотрудников фирмы: '))
    profit_per_worker = profit / workers_q
    print('Прибыль из расчета на 1 сотрудника составила: ', profit_per_worker)

else:
    print('Ваша фирма работает с убытком')