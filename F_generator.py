def my_gen(start, end):
    value = start

    while value < end:
        yield value
        value += 2

if __name__ == '__main__':
    gen = my_gen(0, 10)

    for num in gen:
        print(num, end=' ')