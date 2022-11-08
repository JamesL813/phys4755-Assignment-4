import math


def numerov(m, h, u0, u1, q, s):
    u = [0.0] * (m)
    u[0] = u0
    u[1] = u1
    g = h * h / 12
    i = 1
    while (i < m - 1):
        c0 = 1 + g * q[i - 1]
        c1 = 2 - 10 * g * q[i]
        c2 = 1 + g * q[i + 1]
        d = g * (s[i + 1] + s[i - 1] + 10 * s[i])
        u[i + 1] = (c1 * u[i] - c0 * u[i - 1] + d) / c2
        print(i*h, u[i+1], sep=",")
        i += 1
    return u


def upp(ux):
    return -4*(math.pi**2)*ux


def u(uppx):
    return uppx/(-4*math.pi**2)


if __name__ == "__main__":
    m = 100
    h = 0.1

    q = [4*math.pi] * m
    s = [0.0] * m

    u0 = 1.0
    up0 = 0.0
    upp0 = upp(u0)

    u1 = u0 + up0 + upp0*0.5
    print("x,u")
    numerov(m, h, u0, u1, q, s)
