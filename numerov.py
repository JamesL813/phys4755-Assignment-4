import math


def numerov(m, h, u0, u1, q, s):
    u = [0.0] * (m)
    u[0] = u0
    u[1] = u1
    g = h * h / 12
    i = 1
    y = [0.0] * (2)
    y[0] = u0
    y[1] = u1
    print(0.0, u[0], actual(0), sep=",")
    print(1.0, u[1], actual(1), sep=",")
    while (i < m - 1):
        c0 = 1 + g * q[i - 1]
        c1 = 2 - 10 * g * q[i]
        c2 = 1 + g * q[i + 1]
        d = g * (s[i + 1] + s[i - 1] + 10 * s[i])
        u[i + 1] = (c1 * u[i] - c0 * u[i - 1] + d) / c2
        y = rungeKutta(y, i, 1)
        print(y[1])
        i += 1
    return u


def rungeKutta(y,  t,  dt):
    # Method to complete one Runge-Kutta step.
    n = len(y)
    c1 = [0.0] * (n)
    c2 = [0.0] * (n)
    c3 = [0.0] * (n)
    c4 = [0.0] * (n)
    c1 = g(y, t)
    i = 0
    for i in range(n):
        c2[i] = y[i] + dt * c1[i] / 2
    c2 = g(c2, t + dt / 2)
    i = 0
    for i in range(n):
        c3[i] = y[i] + dt * c2[i] / 2
    c3 = g(c3, t + dt / 2)
    i = 0
    for i in range(n):
        c4[i] = y[i] + dt * c3[i]
    c4 = g(c4, t + dt)
    i = 0
    for i in range(n):
        c1[i] = y[i] + dt * (c1[i] + 2 * (c2[i] + c3[i]) + c4[i]) / 6
    return c1


def upp(ux):
    return -4*(math.pi**2)*ux


def u(uppx):
    return uppx/(-4*math.pi**2)


def g(y,  t):
    k = len(y)
    v = [0.0] * (k)
    v[0] = y[1]
    v[1] = -4 * math.pi**2 * (y[0])
    return v


def actual(x):
    a = 1.41
    b = .355

    return upp(a*math.sin(b*x))


if __name__ == "__main__":
    m = 100
    h = 0.1

    q = [4*math.pi] * m
    s = [0.0] * m

    u0 = 1.0
    up0 = 0.0
    upp0 = upp(u0)

    u1 = u0 + up0 + upp0*0.5
    print("x,u,actual")
    numerov(m, h, u0, u1, q, s)
