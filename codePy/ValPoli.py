def calcValue(Expr, x):
    res = Expr[-1]
    for a in range(len(Expr) - 1):
        res = res * x + Expr[-2 - a]
    return res


print(calcValue([1, 2, 3], 2))
