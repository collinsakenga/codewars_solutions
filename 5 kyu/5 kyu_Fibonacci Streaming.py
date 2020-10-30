def all_fibonacci_numbers():
    yield 1
    yield 1
    a = b = 1
    while True:
        a, b = b, a+b
        yield b