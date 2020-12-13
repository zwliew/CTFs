p = 26513
q = 32321


def solve(a, b):
    x, y = 1, 0
    x1, y1 = 0, 1
    a1, b1 = a, b

    while b1:
        q = a1 // b1
        a1, b1 = b1, a1 - q * b1
        x, x1 = x1, x - q * x1
        y, y1 = y1, y - q * y1

    return x, y, a1


print(solve(p, q))
