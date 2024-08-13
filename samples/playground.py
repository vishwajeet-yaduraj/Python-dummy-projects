def add(*args):
    total_sum = 0
    for n in args:
        total_sum += n

    return total_sum


result = add(2, 4, 5, 0, 9, -1, 9)


def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    n -= kwargs["subtract"]

    return n


total = calculate(29, add=5, multiply=3, subtract=4)

print(total)
