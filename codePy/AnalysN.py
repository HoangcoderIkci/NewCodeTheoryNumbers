import math


def method1(n, c, res, x_0=2):
    d = 0
    m = int(4 * (4 * (c**2) * n) ** (1 / 4)) + 1
    print("m : ", m)
    X = [x_0]
    for h in range(m):
        for i in range(2**h, 2 ** (h + 1)):
            X.append((X[i - 1] ** 2 - 1) % n)
            d = int(math.gcd(X[2**h - 1] - X[i], n))
            if d != 1 and d != n:
                res = method1(d, c, res)
                res = method1(int(n / d), c, res)
                return res
    res.append(n)
    return res


res = []


def method2(n, res):
    n = int(n)
    z = int(n ** (0.25)) + 1
    for r in range(z):
        temp = 1
        for j in range(1, z + 1):
            if temp == 0:
                break
            temp = (temp * (r * z + j)) % n
        print(temp)
        d = int(math.gcd(n, temp))
        if d != 1:
            for j in range(1, z + 1):
                if r * z + j != 1 and d % (r * z + j) == 0:
                    print(r * z + j)
                    res.append(r * z + j)
                    d /= r * z + j
                    n /= r * z + j
            res = method2(int(n), res)
            return res
    res.append(n)
    return res


method1(2701, 4,res)
# method2(120, res)

print(res)
