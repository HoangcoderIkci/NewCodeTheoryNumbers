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


def UCLN_u_v_in_MOD(A, B, MOD):
    A = int(abs(A))
    B = int(abs(B))
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
    return (g * y)% MOD, G% MOD , H % MOD

def process1(A, so_mu, l, r, w, t, n, d, res, MOD):
    m = r - l + 1
    #print(l, r)
    temp = int(m / 2)
    A_cp = A.copy()
    c1 = (w**so_mu) % MOD
    c2 = (w ** (so_mu + n / 2)) % MOD
    for i in range(l, l + temp):
        A_cp[i] = (A[i] + c1 * A[i + temp]) % MOD
        A_cp[i + temp] = (A[i] + c2 * A[i + temp]) % MOD
    #print(A_cp)
    if t < d:
        A_cp, res = process1(A_cp, so_mu / 2, l, l + temp - 1, w, t + 1, n, d, res, MOD)
        A_cp, res = process1(
            A_cp, (so_mu + n / 2) / 2, l + temp, r, w, t + 1, n, d, res, MOD
        )
    else:
        res[int(so_mu)] = A_cp[l]
        res[int((so_mu + n / 2))] = A_cp[r]
    return A_cp, res


def find_bgph(A, n, w, *, d, res, MOD):
    r = len(A) - 1
    A_res, res = process1(A, 0, 0, r, w, 1, n, d, res, MOD)
    # qua trinh 2 tim n^-1
    d, u, v = UCLN_u_v_in_MOD(n, MOD, MOD=MOD)
    # print(u, v)
    res_cp = res.copy()
    for i in range(len(res)):
        res[i] = Nhan_trong_module(u, res[i], Module=MOD)
    l_temp = res.copy()[1:]
    l_temp.reverse()
    hs_polymian = [res[0]] + l_temp
    return A_res, res_cp, hs_polymian

def multipleTwoPolynomialver1(F_input,G_input,w,module):
    F = []
    G = []
    for elem in F_input:
        F.append(elem)
    for elem in G_input:
        G.append(elem)
        
    deg_sum = len(G) + len(F) - 2
    d = int(math.ceil(math.log(deg_sum+1, 2)))
    n = 2**d
    F.extend([0] * (n - len(F)))
    G.extend([0] * (n - len(G)))
    # buoc 2 tinh gia tri cua F
    res1 = [0] * n
    _, res1, hs_pl = find_bgph(F, n, w, d=d, res=res1, MOD=module)
    # buoc 3 tinh gia tri cua G
    res2 = [0] * n
    _, res2, hs_p2 = find_bgph(G, n, w, d=d, res=res2, MOD=module)
    # buoc 4 nhan toa do 2 gia tri cua F va G
    pl1 = res1
    pl2 = res2
    tich_toa_do = []
    if len(pl1) <= len(pl2):
        tich_toa_do = pl2.copy()
        for i in range(len(pl1)):
            tich_toa_do[i] = Nhan_trong_module(pl1[i], tich_toa_do[i], Module=module)
    else:
        tich_toa_do = pl1.copy()
        for i in range(len(pl2)):
            tich_toa_do[i] = Nhan_trong_module(pl2[i], tich_toa_do[i], Module=module)
            
    #print(tich_toa_do)
    res3 = [0] * n
    _, _, hspl3 = find_bgph(tich_toa_do, n, w, d=d, res=res3, MOD=module)
    #print(hspl3)
    flag = 0
    for id in range(len(hspl3)):
        if hspl3[len(hspl3)-1-id] != 0:
            flag = id
            break
    return hspl3[:len(hspl3)-id]
    #return hspl3

def multipleTwoPolynomialverSupper(F_input,G_input,w,module):
    F = []
    G = []
    for elem in F_input:
        F.append(elem)
    for elem in G_input:
        G.append(elem)
    deg_sum = len(G) + len(F) - 2
    d = int(math.ceil(math.log(deg_sum+1, 2)))
    n = 2**d
    M = w**(n >> 1) + 1
    #M = module
    F.extend([0] * (n - len(F)))
    G.extend([0] * (n - len(G)))
    # buoc 2 tinh gia tri cua F
    res1 = [0] * n
    _, res1, hs_pl = find_bgph(F, n, w, d=d, res=res1, MOD=M)
    # buoc 3 tinh gia tri cua G
    res2 = [0] * n
    _, res2, hs_p2 = find_bgph(G, n, w, d=d, res=res2, MOD=M)
    # buoc 4 nhan toa do 2 gia tri cua F va G
    pl1 = res1
    pl2 = res2
    tich_toa_do = []
    if len(pl1) <= len(pl2):
        tich_toa_do = pl2.copy()
        for i in range(len(pl1)):
            tich_toa_do[i] = Nhan_trong_module(pl1[i], tich_toa_do[i], Module=M)
    else:
        tich_toa_do = pl1.copy()
        for i in range(len(pl2)):
            tich_toa_do[i] = Nhan_trong_module(pl2[i], tich_toa_do[i], Module=M)
            
    #print(tich_toa_do)
    res3 = [0] * n
    _, _, hspl3 = find_bgph(tich_toa_do, n, w, d=d, res=res3, MOD=M)
    #print(hspl3)
    flag = 0
    for id in range(len(hspl3)):
        if hspl3[len(hspl3)-1-id] != 0:
            flag = id
            break
    hspl3 = hspl3[:len(hspl3)-id]
    for id in range(len(hspl3)):
        hspl3[id] %= module
    return hspl3

def multipleTwoPolynomial(F_cp,G_cp,w,n,d,module):
    deg_sum = len(F_cp) + len(G_cp) - 2
    F = []
    G = []
    for elem in F_cp:
        F.append(elem)
    for elem in G_cp:
        G.append(elem)
    
    #d = int(math.ceil(math.log(deg_sum+1, 2)))
    #n = 2**d
    F.extend([0] * (n - len(F)))
    G.extend([0] * (n - len(G)))
    # buoc 2 tinh gia tri cua F
    res1 = [0] * n
    _, res1, hs_pl = find_bgph(F, n, w, d=d, res=res1, MOD=module)
    # buoc 3 tinh gia tri cua G
    res2 = [0] * n
    _, res2, hs_p2 = find_bgph(G, n, w, d=d, res=res2, MOD=module)
    # buoc 4 nhan toa do 2 gia tri cua F va G
    pl1 = res1
    pl2 = res2
    tich_toa_do = []
    if len(pl1) <= len(pl2):
        tich_toa_do = pl2.copy()
        for i in range(len(pl1)):
            tich_toa_do[i] = Nhan_trong_module(pl1[i], tich_toa_do[i], Module=module)
    else:
        tich_toa_do = pl1.copy()
        for i in range(len(pl2)):
            tich_toa_do[i] = Nhan_trong_module(pl2[i], tich_toa_do[i], Module=module)
            
    #print(tich_toa_do)
    res3 = [0] * n
    _, _, hspl3 = find_bgph(tich_toa_do, n, w, d=d, res=res3, MOD=module)
    #print(hspl3)

    return hspl3
################## BEGIN function chia da thuc ##################
def InverseCoefficients(F_x,taget_degree):
    NewF_x = [0] * (taget_degree+1)
    for id in range(min(len(F_x),taget_degree+1)):
        NewF_x[-1-id] = F_x[id]
    return NewF_x
        
    
def PhiSupport(A_x,G_x,module,w=2):
    # a(x) (2-a*g)
    #b1 tinh a*g:
    #mult_a_g = multipleTwoPolynomial(A_x,G_x,w,N,d,module)
    mult_a_g = multipleTwoPolynomialverSupper(A_x,G_x,w,module)
    # 2 - a*g:
    mult_a_g[0] = mult_a_g[0] - 2
    for idx in range(len(mult_a_g)):
        mult_a_g[idx] = (-mult_a_g[idx])%module
    #b3 tinh a(x) (2-a*g)
    res = multipleTwoPolynomialverSupper(A_x,mult_a_g,w,module)
    #print(res)
    return res

def getRemainderDivider(F_x,G_x,MOD):
    deg_F = len(F_x)-1
    m = len(G_x) - 1
    d = int(math.ceil(math.log(deg_F, 2)))
    N = 2**d
    w = 2
    #F_x.extend([0] * (N-len(F_x)))
    #deg_F = N-1
    #b0 tinh k : 2^(k-1) <= n-m < 2^k
    k = int(math.log2(deg_F-m)) + 1
    #module = w**(N >> 1) + 1
    module = MOD
    #b1 : dao nguoc tat ca he so cua F va G
    F_x_inv = InverseCoefficients(F_x,deg_F)
    G_x_inv = InverseCoefficients(G_x,m)
    #b2 tim G[-1]^-1
    _,P_x,_ = UCLN_u_v_in_MOD(G_x[-1],module,module)
    P_x = [P_x]
    #b3 tinh P_k 
    for i in range(2,k+2):
        P_x = PhiSupport(P_x,G_x_inv,module)
        #(P_x)
        P_x = P_x[:(1 << i)]
        #print(P_x)
    # da co H_x = P_x
    #b4 tinh Q_x = P_x * F_x_inv
    P_x = P_x[:(1 << k)]
    Q_x = multipleTwoPolynomialverSupper(F_x_inv,P_x,w,module)
    #b5 tinh Q_x mod (x ^ (deg_F-m+1))
    Q_x = Q_x[:deg_F-m+1]
    #b6 revers Q_x 
    Q_x = InverseCoefficients(Q_x,deg_F-m)
    print(f"Q_x = {Q_x}")
    #b7 tinh R_x = F_x_ - Q_x * G_x
    Q_x_G_x = multipleTwoPolynomialverSupper(Q_x,G_x,w,module)
    R_x = []
    for id in range(m):
        R_x.append((F_x[id]-Q_x_G_x[id])%module)
    print(f"R_x = {R_x}")
################## END function chia da thuc ##################
import sympy as sp

def multiply_polynomials(coeffs1, coeffs2):
    # Định nghĩa biến
    x = sp.symbols('x')
    
    # Tạo hàm số từ các hệ số
    poly1 = sum(c * x**i for i, c in enumerate(coeffs1))
    poly2 = sum(c * x**i for i, c in enumerate(coeffs2))
    
    # Nhân hai hàm số
    product = sp.expand(poly1 * poly2)
    return product
    #return[x % 3 for x in  list(product.as_coefficients_dict().values()) ]

if __name__ == '__main__':
    # w = 2
    # module = 17
    # pl1 = [1, 3, 2, 0, 1]
    # pl2 = [1, 1, 0, 2]
    # multipleTwoPolynomial(pl1,pl2,w,module)
    from random import randint
    # F = []
    # G = []
    # for id in range(4):
    #     F.append(randint(0,2))
    # for id in range(2):
    #     G.append(randint(0,2))
    # print(F)
    # print(G)
    #getRemainderDivider(F,G,3)
    # [11, 6, 12, 1, 14]   
    #  0, 1, 6, 1, 14
    # [4, 4, 1]
    # Q_x = [0, 13, 14, 0, 0, 0]
    # R_x = [11, 5]
    F = [1, 1,1, 1]
    G = [1, 2]
    getRemainderDivider(F,G,7)
    print(multipleTwoPolynomialverSupper(F,G,2,17))
    print(multiply_polynomials(F,G))