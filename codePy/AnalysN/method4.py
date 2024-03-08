import numpy as np
import math
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
    return (g * y) , G , H 
def kiem_tra_binh_phuong(a, b):
    # a = 7
    # b = 5
    if a % b == 0:
        return 0
    if b == 2:
        return a &0b1
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



def PrimeFactorDecompositionF_B(c):
    alpha = []
    _alpha = []
    if global_F_B[0] != -1:
        for p in global_F_B:
            count = 0
            while c % p == 0:
                count += 1
                c //= p
            alpha.append(count)
            _alpha.append(count&0x1)
        if c!=1:
            return False
        return alpha,_alpha
    else:
        if c < 0:
            c*=-1
            alpha.append(1)
            _alpha.append(1)
        else:
            alpha.append(0)
            _alpha.append(0)
        for p in global_F_B[1:]:
            count = 0
            while c % p == 0:
                count += 1
                c //= p
            alpha.append(count)
            _alpha.append(count&0x1)
        if c!=1:
            return False
        return alpha,_alpha
def checkLinearDependence(mt):
    mt1 = np.array(mt)
    mt1 = mt1.transpose()
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
                break
            elif row == num_rows-1:
                res = list(mt1[:,col])
                res = res[:col]
                res.append(1)
                return res
    # if rank != num_cols:
    #     return lst_ind_basic
    return False
# b5 
def b5(lst_basic):
    X = 1
    for id in range(len(lst_basic)):
        if lst_basic[id] != 0:
            X = Nhan_trong_module(X,G_setA[id],global_N)
    Y = 1
    pow_p_j = 0
    for j in range(len(global_F_B)):
        pow_p_j = 0
        for id in range(len(lst_basic)):
            if lst_basic[id] != 0:
                alpha = G_setAlpha[id]
                pow_p_j += alpha[j]
        pow_p_j >>=1
        Y = Nhan_trong_module(Y,global_F_B[j]**pow_p_j,global_N)
    return X,Y
def b6(X,Y):
    d,_,_ = UCLN_u_v(X-Y,global_N)
    return d
def ProperFraction(d,u,v):
    if (d**(0.5) - u) % v !=0:
        d *= v**2
        u *= abs(v)
    D = d
    sqrtD = d**(0.5)
    V = [v]
    A = [(d**(0.5) - u)//v]
    U = [u+A[0]*v]
    P = [1,A[0]]
    Q = [0,1]
    v_temp = 0
    flag = 0
    for i in range(10000):
        V.append( (D - U[i]**2) // V[i])
        A.append(int((sqrtD + U[i]) / V[i+1]))
        U.append(A[i+1]*V[i+1] - U[i])
        P.append((P[i+1] * A[-1] + P[i])%global_N)
        Q.append(Q[i+1] * A[-1] + Q[i])
        v_temp = (-1) **(i+1) * V[-1]
        flag = PrimeFactorDecompositionF_B(v_temp)
        if flag != False:
            G_setA.append(P[-2])
            G_setAlpha.append(flag[0])
            G_setAlpha_support.append(flag[1])
            flag = checkLinearDependence(G_setAlpha_support)
            if flag != False:
                X,Y = b5(flag)
                d = b6(X,Y)
                print(d)
                return
if __name__ == "__main__":
    # variable 
    import random as rd
    global_N = 164227511
    B = int(2.7**(0.5 * math.sqrt(math.log(global_N)*math.log(math.log(global_N)))))
    F_B_temp = sieve_of_eratosthenes(B)
    print(global_N)
    #global_N = 133806
    global_F_B = []
    G_setAlpha = []
    G_setAlpha_support = []
    G_setA = []
    flag = 1
    for p in F_B_temp:
        if kiem_tra_binh_phuong(global_N,p) == 1:
            global_F_B.append(p)
        else:
            flag = 0
    if flag == 0:
        global_F_B.insert(0,-1)
    ProperFraction(global_N,0,1)
