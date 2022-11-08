import math


def secant(n, delta,  x,  dx):
    # Method to carry out the secant search.
    k = 0
    x1 = x + dx
    while ((abs(dx) > delta) and (k < n)):
        d = f(x1) - f(x)
        x2 = x1 - f(x1) * (x1 - x) / d
        x = x1
        x1 = x2
        dx = x1 - x
        k += 1
    if (k == n):
        print("Convergence not" + " found after " + str(n) + " iterations")
    return x1


def f(x):
    # Method to provide the function for the root search.
    y = [0.0] * (2)
    y[0] = 0
    y[1] = x
    i = 0
    while (i < n - 1):
        xi = h * i
        y = rungeKutta(y, xi, h)
        i += 1
    return y[0] - 1


def rungeKutta(y,  t,  dt):
    # Method to complete one Runge-Kutta step.
    l = len(y)
    c1 = [0.0] * (l)
    c2 = [0.0] * (l)
    c3 = [0.0] * (l)
    c4 = [0.0] * (l)
    c1 = g(y, t)
    i = 0
    while (i < l):
        c2[i] = y[i] + dt * c1[i] / 2
        i += 1
    c2 = g(c2, t + dt / 2)
    i = 0
    while (i < l):
        c3[i] = y[i] + dt * c2[i] / 2
        i += 1
    c3 = g(c3, t + dt / 2)
    i = 0
    while (i < l):
        c4[i] = y[i] + dt * c3[i]
        i += 1
    c4 = g(c4, t + dt)
    i = 0
    while (i < l):
        c1[i] = y[i] + dt * (c1[i] + 2 * (c2[i] + c3[i]) + c4[i]) / 6
        i += 1
    return c1
# Method to provide the generalized velocity vector.


def g(y,  t):
    k = len(y)
    v = [0.0] * (k)
    v[0] = y[1]
    v[1] = -math.pi * math.pi * (y[0] + 1) / 4
    return v


if __name__ == "__main__":
    n = 100
    ni = 10
    m = 5
    h = 1.0 / n
    delta = 1.0e-6
    alpha0 = 1
    dalpha = 0.01
    y1 = [0.0] * (n + 1)
    y2 = [0.0] * (n + 1)
    y = [0.0] * (2)
    # Search the proper solution of the equation
    y1[0] = 0
    y[0] = 0
    y2[0] = secant(ni, delta, alpha0, dalpha)
    y[1] = y2[0]
    i = 0
    while (i < n):
        x = h * i
        y = rungeKutta(y, x, h)
        y1[i + 1] = y[0]
        y2[i + 1] = y[1]
        i += 1
    # Output the result in every m points
    i = 0
    while (i <= n):
        print(y1[i])
        i += m
