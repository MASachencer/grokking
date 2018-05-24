def fact(x):
    while x > 1:
        return x * fact(x - 1)
    else:
        return x


def fact2(x):
    a, b = x, x - 1
    while b > 1:
        a, b = a * b, b - 1
    return a


print(fact(5))
print(fact2(5))
