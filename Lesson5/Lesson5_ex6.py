my_dict = {}
with open('ex6_file.txt') as f:
    list_of_lines = f.readlines()
    for i, line in enumerate(list_of_lines):
        list_of_words = line.split()
        sum_hours = 0
        for u in list_of_words:
            index_slice = u.find('(')
            if index_slice != -1:
                hours = int(u[0:index_slice])
                sum_hours = sum_hours + hours
        my_dict[f'{list_of_words[0][:-1]}'] = sum_hours

print(my_dict)