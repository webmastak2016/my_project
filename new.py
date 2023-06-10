def logged_func(func):
    def inner(x, y):
        print(f'called with {x}, {y}')
        result = func(x, y)
        print(f'result: {result}')
        return result
    return inner


@logged_func
def complicated(x, y):
    return x / y


complicated(1, 2)
