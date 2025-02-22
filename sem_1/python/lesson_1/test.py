import math


def f(x: int):
    return math.factorial(x)


a = f(10) / (f(2) * f(3) * f(2))
print(a)
