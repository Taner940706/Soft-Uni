def cache(func):
    log = {}

    def wrapper(number):
        if number in log:
            return log[number]
        result = func(number)
        log[number] = result

        return result

    wrapper.log = log
    return wrapper