seconds = int(input('Введите количество секунд: '))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

result = f'Результат: {hours}:{minutes}:{seconds}'
print(result)