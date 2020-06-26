with open('ex2_file.txt') as f:
    lines = f.readlines()
    print(lines)
    print(f'Количество строк в файле: {len(lines)} ')
    for i,line in enumerate(lines):
        print(f'{i+1} строка: {len(line.split())} слов(а)')



