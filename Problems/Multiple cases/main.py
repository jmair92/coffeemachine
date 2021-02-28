import math


def f1(x):
    a = math.pow(x, 2) + 1
    if a is None:
        return 0.0
    else:
        return a


def f2(x):
    a = 1 / math.pow(x, 2)
    if a is None:
        return 0.0
    else:
        return a


def f3(x):
    a = math.pow(x, 2) - 1
    if a is None:
        return 0.0
    else:
        return a


def f(x):
    if x <= 0:
        return f1(x)
    elif 0 < x < 1:
        return f2(x)
    else:
        return f3(x)
