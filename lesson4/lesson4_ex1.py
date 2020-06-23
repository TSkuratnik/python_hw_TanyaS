import sys


def salary():
    args = sys.argv[1:]
    result = int(args[0]) * int(args[1]) + int(args[2])
    print(f'Доход сотрудника составил {result}')
    return result


salary()