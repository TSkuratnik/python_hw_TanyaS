import json
sum_profit = 0
q_profit_firms = 0
firm_profit_dict = {}
avarage_profit_dict = {}
my_result_list = [firm_profit_dict, avarage_profit_dict]

with open('ex7_file.txt') as f:
    list_of_lines = f.readlines()
    print(list_of_lines)
    for i, line in enumerate(list_of_lines):
        list_of_words = line.split()
        print(list_of_words)
        profit = int(list_of_words[2]) - int(list_of_words[3])
        print(profit)
        print(list_of_words[0])
        firm_profit_dict[f'{list_of_words[0]}'] = profit
        if profit > 0:
            sum_profit = sum_profit + profit
            q_profit_firms = q_profit_firms + 1
    avarage_profit = sum_profit / q_profit_firms
    print(f'средняя прибыль = {avarage_profit}')
    avarage_profit['Средняя прибыль'] = avarage_profit

    print(avarage_profit)
    print(firm_profit_dict)
    print(my_result_list)
    json.dump(my_result_list, 'ex7_json.txt')