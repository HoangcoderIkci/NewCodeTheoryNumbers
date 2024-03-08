from math import gcd
import math
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
def powInModule(a,power,module):
    #power
    res = a if power &0b1 else 1
    turn = int(math.log(power,2))
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
# Hàm tính bội chung nhỏ nhất của 2 số
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Hàm tính bội chung nhỏ nhất của n số
def lcm_of_n_numbers(numbers):
    lcm_result = numbers[0]
    for i in range(1, len(numbers)):
        lcm_result = lcm(lcm_result, numbers[i])
    return lcm_result

def PollardMethod(B,N):
    F_B = sieve_of_eratosthenes(B)
    k = lcm_of_n_numbers(F_B)
    for a in range(2,N-1):
        c = powInModule(a,k,N)
        d,_,_ = UCLN_u_v(c-1,N)
        if d != 1 and d != N:
            print(d)
            return d
        
if __name__ == "__main__":
    
    B = 8
    N = 312315425131312313
    PollardMethod(B,N)