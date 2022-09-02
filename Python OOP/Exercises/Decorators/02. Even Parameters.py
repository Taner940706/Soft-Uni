def even_parameters(func_ref):

    def wrapper(*args):
        for element in args:
            if not isinstance(element, int) or element % 2 != 0:
                return 'Please use only even numbers!'
        return func_ref(*args)

    return wrapper