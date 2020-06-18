def degree(x,y):
    """First method"""
    result = x ** y
    print(result)
    return result


degree(3, -3)


def my_degree(x,y):
    """Second method"""
    result = 1
    for i in range(abs(y)):
        result = (1 / x) * result
    print(result)
    return result


my_degree(3, -3)