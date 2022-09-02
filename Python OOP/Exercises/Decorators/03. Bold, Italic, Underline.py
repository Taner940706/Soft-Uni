def make_bold(func_ref):
    def wrapper(*args):
        func_result = func_ref(*args)
        return f'<b>{func_result}</b>'

    return wrapper


def make_italic(func_ref):
    def wrapper(*args):
        func_result = func_ref(*args)
        return f'<i>{func_result}</i>'

    return wrapper


def make_underline(func_ref):
    def wrapper(*args):
        func_result = func_ref(*args)
        return f'<u>{func_result}</u>'

    return wrapper