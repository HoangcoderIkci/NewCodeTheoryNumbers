from math import gcd,ceil,log
from random import randint
def Nhan_trong_module(A, B, Module):
    if Module &0b1 != 1:
        return (A*B) % Module
    A = int(A)
    B = int(B)
    Module = int(Module)
    n = ceil(log(Module, 2))
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
def UCLN_u_v(A, B):
    A = abs(A)
    B = abs(B)
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
    return (g * y) , G , H 
def powInModule(a,power,module):
    #power
    res = a if power &0b1 else 1
    turn = int(log(power,2))
    id1 = 0
    power >>=1
    while id1 < turn:
    #for id1 in range(turn):
        a = Nhan_trong_module(a,a,module)
        if power&0b1:
            res = Nhan_trong_module(res,a,module)
        power>>=1
        if a == 1:
            return res
        if power == 1:
            break
    if id1 < turn:
        a = Nhan_trong_module(a,a,module)
        res = Nhan_trong_module(res,a,module)
        
    return res
def createF(lst_primer_F):
    F = 1
    for q in lst_primer_F:
        k = randint(2,5)
        #F = Nhan_trong_module(F,powInModule(q,k,MOD),MOD)
        F *= q **k
    return F
def createN(lst_primer_F):
    F = 1
    temp1 = 4
    temp2 = 1
    while temp1 > 0 and temp2.is_integer(): 
        y = randint(2,10)
        x = randint(2,10)
        temp1 = y**2 - 4*x
        temp2 = temp1 ** (0.5)
    # check dk
    F = createF(lst_primer_F)
    N = (x*F+y) * F + 1
    print(N)
    # for q in lst_primer_F:
    #     if not checkQ(q,N):
    #         print(False)
    #         return False
    # print(N)
    # return N
def check1(Q,N):
    #bina = bina(N) 
    #turn = 0
    Q = Nhan_trong_module(Q,Q,N)
    res = Q
    #Q = Nhan_trong_module(Q,Q,N)
    N_temp = N-1
    N_temp >>= 2
    while N_temp>1:
        Q = Nhan_trong_module(Q,Q,N)
        if N_temp&0b1:
            res = Nhan_trong_module(res,Q,N)
        #turn+=1
        if res == 1:
            return True
        N_temp >>= 1
    #return Q == 1
    Q = Nhan_trong_module(Q,Q,N)
    res = Nhan_trong_module(res,Q,N)
    return res == 1
    #return False
def checkQ(q,N):
    a = -1
    for idx1 in range(2,N):
        if gcd(idx1,N) == 1 :
            if check1(idx1,N):
                temp = powInModule(idx1,(N-1)//q,N)
                if gcd(temp - 1,N) == 1:
                    a = idx1
                    return True
    return False

N = 312315425131312313
# checkQ(5,N)

x_ = randint(2,10)
y_ = randint(2,10)
# print(5 **(N-1)%N)
print(powInModule(5,N-1,N))

# createN([5,3])