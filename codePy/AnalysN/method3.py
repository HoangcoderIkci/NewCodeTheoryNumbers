import math
import numpy as np
# các hàm hỗ trợ
def Nhan_trong_module(A, B, Module):
    if Module &0b1 != 1:
        return (A*B) % Module
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
    res = a
    for turn in range(power-1):
        res = Nhan_trong_module(res,a,module)
    return res
# Method ferma
def ferma(n,p):
    sqRootN = n**(0.5)
    X,temp=0
    for k in range(100):
        X = sqRootN + k
        Y = X**2 - n
        square_root = math.sqrt(Y)
        if square_root.is_integer():
            return X+Y
    return 0

################# Begin thuật toán Диксона #################### 
# Global variables
N = 1739
B = int(2.7**(0.5 * math.sqrt(math.log(N)*math.log(math.log(N)))))
def sieve_of_eratosthenes(n):
    # Tạo một mảng boolean, đánh dấu tất cả số như là số nguyên tố (True)
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        # Nếu prime[p] không bị thay đổi, thì nó là một số nguyên tố
        if (prime[p] == True):
            # Đánh dấu tất cả bội số của p từ p^2 đến n như không phải là số nguyên tố
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # In ra các số nguyên tố
    prime_numbers = []
    for p in range(n+1):
        if prime[p]:
            prime_numbers.append(p)
    return prime_numbers
F_B = sieve_of_eratosthenes(B)
g_h = len(F_B)
G_setAlpha = []
G_setAlpha_support = []
G_setA = []
def PrimeFactorDecompositionF_B(c):
    alpha = []
    _alpha = []
    for p in F_B:
        count = 0
        while c % p == 0:
            count += 1
            c //= p
        alpha.append(count)
        _alpha.append(count&0x1)
    if c!=1:
        return False
    # flag = False
    # for elem in _alpha:
    #     if elem != 0:
    #         flag = 1
    #         break
    # if flag == False:
    #     return False
    return alpha,_alpha

def checkLinearDependence(mt):
    mt1 = np.array(mt)
    rank = 0
    lst_ind_basic = []
    # Lấy kích thước số hàng và cột của ma trận
    num_rows, num_cols = mt1.shape
    for col in range(num_cols):
        for row in range(rank, num_rows):
            if mt1[row][col]:
                lst_ind_basic.append(col)
                if row != rank:
                    temp_row = mt1[row].copy()
                    # print(temp_row)
                    mt1[row] = mt1[rank]
                    # print(temp_row)
                    mt1[rank] = temp_row
                   
                    # mt1[row], mt1[rank] = mt1[rank], mt1[row]
                    # print(mt1)
                #hs_nghich_dao = arrInverseSubtraction2[mt1[rank][col]]
                # đưa hệ số về 1
                # ap null các rows ở dưới row rank:
                for idr in range(rank + 1, num_rows):
                    if mt1[idr][col]:
                        for idcl in range(col, num_cols):
                            mt1[idr][idcl] ^=mt1[rank][idcl]
                rank += 1
            # else:
            #     return False
    return rank != num_rows
    #return True
    
# b5 
def b5():
    X = 1
    for a in G_setA:
        X = Nhan_trong_module(X,a,N)
    Y = 1
    pow_p_j = 0
    for j in range(g_h):
        pow_p_j = 0
        for alpha in G_setAlpha:
            pow_p_j += alpha[j]
        pow_p_j >>=1
        Y = Nhan_trong_module(Y,F_B[j]**pow_p_j,N)
    return X,Y
def b6(X,Y):
    d,_,_ = UCLN_u_v(X-Y,N)
    return d
def dicona():
    c = 0
    for a in range(2,N):
        c = Nhan_trong_module(a,a,N)
        lst_al = PrimeFactorDecompositionF_B(c)
        if lst_al != False:
            alpha,_alpha = lst_al
            G_setAlpha.append(alpha)
            G_setAlpha_support.append(_alpha)
            G_setA.append(a)
            isLinearDependence = checkLinearDependence(G_setAlpha_support)
            if isLinearDependence:
                X,Y = b5()
                if X != Y:
                    d = b6(X,Y)
                    if d != 1 and d != N:
                        print(d)
                        return d
                
from sympy import primefactors

def prime_factorization(n):
    factors = primefactors(n)
    return factors            
################# End thuật toán Диксона #################### 
if __name__ == '__main__':
    import random as rd
    N = 16422751
    print(N)
    #B = 100
    d = dicona()
    print(N % d)
    #print(Nhan_trong_module(3,3,120))
    print(prime_factorization(N))