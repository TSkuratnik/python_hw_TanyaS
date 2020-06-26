with open('ex4_file.txt') as f:
    with open('ex4_file_ru.txt', 'w+') as f_ru:
        list_of_lines = f.readlines()
        russian_numbers = ['Один', 'Два', 'Три', 'Четыре']
        for i, line in enumerate(list_of_lines):
            i_list = line.split()
            i_list[0] = russian_numbers[i]
            ru_line = ' '.join(i_list)
            f_ru.writelines(ru_line)
            f_ru.writelines('\n')


