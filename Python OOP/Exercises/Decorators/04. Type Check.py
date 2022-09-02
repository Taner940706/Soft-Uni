def type_check(type):
    def decorator(func_ref):
        def wrapper(param):
            if not isinstance(param, type):
                return 'Bad Type'
            return func_ref(param)

        return wrapper
    return decorator