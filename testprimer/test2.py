#B1 RANDOM
import random

def gcd(A, B):
    g = 1
    _A = A
    _B = B
    while _A % 2 == 0 and _B % 2 == 0:
        _A >>= 1
        _B >>= 1
        g <<= 1
    x, y, E, F, G, H = _A, _B, 1, 0, 0, 1
    while x != 0:
        while x % 2 == 0:
            x >>= 1
            if E % 2 == 0 and F % 2 == 0:
                F >>= 1
                E >>= 1
            else:
                E = (E + _B) >> 1
                F = (F - _A) >> 1
        while y % 2 == 0:
            y >>= 1
            if G % 2 == 0 and H % 2 == 0:
                G >>= 1
                H >>= 1
            else:
                G = (G + _B) >> 1
                H = (H - _A) >> 1
        if x >= y:
            x -= y
            E -= G
            F -= H
        else:
            y -= x
            G -= E
            H -= F

    # print(f"d = {g*y}")
    # print(f"u = {G}")
    # print(f"v = {H}")
    return g * y, G, H

import math


def Nhan_trong_module(A, B, Module):
    A = int(A)
    B = int(B)
    Module = int(Module)
    n = math.ceil(math.log(Module, 2))
    binary_list = [int(i) for i in bin(A)[2:]]
    temp = n - len(binary_list)
    binary_list = [0] * temp + binary_list
    C = (2 ** (2 * n)) % Module
    R = 0
    for i in range(n):
        if binary_list[n - 1 - i] & 0b01:
            R = R + B
        if R & 0b01:
            R += Module
        R >>= 1
    if R >= Module:
        R -= Module
    A, B = R, C
    binary_list = [int(i) for i in bin(A)[2:]]
    temp = n - len(binary_list)
    binary_list = [0] * temp + binary_list
    R = 0
    for i in range(n):
        if binary_list[n - 1 - i] & 0b01:
            R += B
        if R & 0b01:
            R += Module
        R >>= 1
    if R >= Module:
        R -= Module
    return R

def tinh_gia_tri_a_mu_x_in_mod_p(a, x, P):
    # print((a**x) % P)
    # Chuyển số 6 sang dạng nhị phân
    binary = [int(i) for i in bin(x)[2:]][::-1]
    # print(binary)
    # binary = binary.reverse()
    if binary[0] == 0:
        res = 1
    else:
        res = a
    for i in range(1, len(binary)):
        a = Nhan_trong_module(a, a, P)
        # print(a)
        if binary[i] == 1:
            res = Nhan_trong_module(a, res, P)
    # print(res)
    return res

def calcSymApple(a, b):
    # a = 7
    # b = 5
    if a % b == 0:
        return 0
    res = 1
    temp = 0
    while a != 2 and a != 1:
        du = a % b
        if du >= b - du:
            a = b - du
            res *= (-1) ** ((b - 1) / 2)
        else:
            a = du
        while a % 2 == 0:
            a /= 2
            res *= (-1) ** ((b**2 - 1) / 8)
        if a == 1:
            return res
        if a == 0:
            return 0
        temp = a
        a = b
        b = temp
        res *= (-1) ** ((a - 1) * (b - 1) / 4)
    return res

def test2(N):
    a = random.randint(1, N)
    d,_,_ = gcd(a, N)
    print(a)
    if d != 1:
        print(f"not primer(d = {d})")
    else:
        t1 = (tinh_gia_tri_a_mu_x_in_mod_p(a,(N-1) >> 1,N))
        t2 = calcSymApple(a,N)
        if t1!=t2:
            print(f"t = {t1,t2} , not primer")
        else:
            print("dont'n know")


N = 21
test2(N)
