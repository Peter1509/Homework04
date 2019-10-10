import math

def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


def square(x):
    return x * x


def root(x):
    return x / x


def logarithm(x):
    return math.log(x)

def into_file(result):
    f = open("ausgabe.txt", "a")
    f.write("\n"*2 + result)
    f.close()
