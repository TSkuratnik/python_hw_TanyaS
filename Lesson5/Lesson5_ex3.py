with open('ex3_file.txt') as f:
    lines = f.readlines()
    q_lines = len(lines)
    income = 0
    print('Сотрудники с доходом < 20000: ')
    for i, line in enumerate(lines):
        i_line = line.split()
        i_income = float(i_line[2])
        if i_income < 20000:
            print(i_line[0], i_line[1])
        income = income + i_income
    avarage_income = income / q_lines
    print('Средняя зарплата сотрудника составляет: ', avarage_income)

