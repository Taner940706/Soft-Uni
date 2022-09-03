def fibonacci():

    fib0 = 0
    fib1 = 1

    yield fib0
    yield fib1
    while True:
        fib = fib0 + fib1
        yield fib
        fib0, fib1 = fib1,fib