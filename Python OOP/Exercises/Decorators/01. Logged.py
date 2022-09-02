def logged(func_ref):
    def wrapper(*args):
        func_name = func_ref.__name__
        result = func_ref(*args)
        return f'you called {func_name}{args}\nit returned {result}'

    return wrapper