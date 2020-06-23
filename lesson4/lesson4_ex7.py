from math import factorial


def generate_factorial(n):
    for elem in range(n):
        yield factorial(elem)


for el in generate_factorial(6):
    print(el)

