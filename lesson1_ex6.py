a = int(input('Введите сколько км спортсмен пробегает в 1-й день: '))
b = int(input('Введите количество км, которые хотел бы пробегать спортсмен: '))
result_per_day = a
i = 1
while result_per_day <= b:
    print(f'Результат в {i} день составляет {result_per_day}')
    result_per_day = result_per_day * 1.1
    i = i + 1

print(f'Спортсмен сможет пробегать {b} километров не раньше чем на {i} день')