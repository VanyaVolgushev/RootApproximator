from math import cos, sin


def separateRoots(func, a, b, stepFactor):
    pass


def printApproximationResults(name, initial_approx, step_counter, approx, last_segment_length, residual):
    print(f'Method name: {name}\n'
          f'Initial approximation: {initial_approx}\n'
          f'Step count: {step_counter}\n'
          f'Approximation by method: {approx}\n'
          f'Last difference: {last_segment_length}\n'
          f'|f(x)-0|: {residual}')


def getStartingValue(a, b, func, second_derivative):
    step = (b - a) / 1000
    x = a

    while True:
        if func(x) * second_derivative(x) > 0:
            break
        x += step
        if x > b:
            raise Exception('No convergence')

    return x


def bisectionMethod(func, a, b, eps):
    step_counter = 0
    local_a = a
    local_b = b

    while (local_b - local_a) > 2 * eps:
        step_counter += 1
        c = (a + b) / 2
        if func(c) * func(local_a) <= 0:
            local_b = c
        else:
            local_a = c

    approx = (local_a + local_b) / 2
    initial_approx = (a + b) / 2
    residual = func(approx)

    printApproximationResults("Bisection method", initial_approx, step_counter, approx, local_b - local_a, residual)


def newtonMethod(func, derivative, second_derivative, a, b, eps):
    step_counter = 0
    initial_approx = x_prev = getStartingValue(a, b, func, second_derivative)

    while True:
        step_counter += 1
        x_curr = x_prev - func(x_prev) / derivative(x_prev)
        if abs(x_curr - x_prev) < eps:
            break
        x_prev = x_curr

    last_segment_length = x_prev - x_curr
    approx = x_curr
    residual = func(approx)

    printApproximationResults('Newton method', initial_approx, step_counter, approx, last_segment_length, residual)


def modifiedNewtonMethod(func, derivative, second_derivative, a, b, eps):
    step_counter = 0
    initial_approx = x_prev = x0 = getStartingValue(a, b, func, second_derivative)

    while True:
        step_counter += 1
        x_curr = x_prev - func(x_prev) / derivative(x0)

        if abs(x_curr - x_prev) < eps:
            break

        x_prev = x_curr

    last_segment_length = x_prev - x_curr
    approx = x_curr
    residual = func(approx)

    printApproximationResults('Modified Newton method', initial_approx, step_counter, approx, last_segment_length,
                              residual)


def secantMethod(func, a, b, eps):
    step_counter = 0
    x_prev = a
    x_curr = b
    x_next = 0

    while True:
        step_counter += 1
        x_next = x_curr - func(x_curr) * (x_curr - x_prev) / (func(x_curr) - func(x_prev))

        if abs(x_next - x_curr) < eps:
            break

        x_prev = x_curr
        x_curr = x_next

    last_segment_length = x_next - x_curr
    approx = x_next
    initial_approx = (a + b) / 2
    residual = func(approx)

    printApproximationResults('Secant method', initial_approx, step_counter, approx, last_segment_length, residual)


if __name__ == "__main__":
    print('Численные методы решения нелинейных уравнений')
    print('eps = 10^(-7)')
    print('[A ; B] = [-9 ; 1]')
    print('f(x) = 8cos(x) - x - 6')

    function = lambda x: 8 * cos(x) - x - 6
    first_deriv = lambda x: -8 * sin(x) - 1
    second_deriv = lambda x: -8 * cos(x)

    A = float(input("Input A: "))
    B = float(input("Input B: "))
    N = int(input("Input N: "))
    EPS = float(input("Input epsilon: "))
