from math import cos, sin


def separateRoots(func, a, b, stepFactor):
    pass


def approximateByBisection(func, a, b, eps):
    pass


def approximateByNewton(func, derivative, secondDerivative, a, b, eps):
    pass


def approximateByModifiedNewton(func, derivative, secondDerivative, a, b, eps):
    pass


def approximateBySecant(func, a, b, eps):
    pass


if __name__ == "__main__":
    func = lambda x: 8 * cos(x) - x - 6
    first_derivative = lambda x: -8 * sin(x) - 1
    second_derivative = lambda x: -8 * cos(x)

    A = int(input("A: "))
    B = int(input("B: "))
    N = int(input("N: "))
    EPS = float(input("EPS: "))
