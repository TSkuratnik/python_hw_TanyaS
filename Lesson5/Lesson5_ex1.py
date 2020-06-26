with open('ex1_file', 'w+') as f:
    while True:
        text = input('Введите текст: ')
        f.writelines(text + '\n')
        if text == '':
            break

    f.seek(0)
    print(f.read())