import math
import random


def Nhan_trong_module(A, B, Module):
    if Module &0b1 == 0:
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


# print(1 << 5)


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
    # print(binary)


# tinh_gia_tri_a_mu_x_in_mod_p(22, 6, 17)
# a = Nhan_trong_module(13, 8, 17)
# print(a)


def kiem_tra_binh_phuong(a, b):
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


def giai_phuong_trinh_binh_phuong(a, P):
    # x^2 = a (p)
    # buoc 1 : kiem tra co nghiem khong
    kt = kiem_tra_binh_phuong(a, P)
    if kt != 1:
        return f"Phuong trinh vo nghiem vi (a/p) = {kt}"
        # return ("vo")
    else:
        # buoc 2 : chia du cho 4
        remain = P % 4
        if remain == 3:
            n_1 = tinh_gia_tri_a_mu_x_in_mod_p(a, int((P + 1) / 4), P)
            return n_1, (P - n_1) % P
        else:
            # buoc 3 truong hop P = 1 mod 4:
            # tim s,t
            t = P - 1
            s = 0
            while t % 2 == 0:
                t /= 2
                s += 1
            print(f"s : {s},t : {t}")
            a_t = tinh_gia_tri_a_mu_x_in_mod_p(a, int(t), P)
            print(f"a_t : {a_t}")
            if a_t == 1:
                n_1 = tinh_gia_tri_a_mu_x_in_mod_p(a, int((t + 1) / 2), P)
                return n_1, (P - n_1) % P
            # tim ngau nhien b de (b/P) != 1
            b = random.randint(1, P)
            while kiem_tra_binh_phuong(b, P) == 1:
                b = random.randint(1, P)
            print(f" b : {b}")
            g = tinh_gia_tri_a_mu_x_in_mod_p(b, int(t), P)
            c = tinh_gia_tri_a_mu_x_in_mod_p(b, 2, P)
            print(f" g : {g}, c : {c}")
            j = 0
            mu = 1 << s - 2
            for k in range(s - 1):
                c = tinh_gia_tri_a_mu_x_in_mod_p(c, j, P)
                temp1 = tinh_gia_tri_a_mu_x_in_mod_p(c, mu, P)
                temp2 = tinh_gia_tri_a_mu_x_in_mod_p(a_t, mu, P)
                r_temp = tinh_gia_tri_a_mu_x_in_mod_p(temp2, temp1, P)
                mu >>= 1
                if r_temp != 1:
                    j += 1 << k
                print(f"j hiện tại : {j}")
            r_1 = Nhan_trong_module(
                tinh_gia_tri_a_mu_x_in_mod_p(g, j, P),
                tinh_gia_tri_a_mu_x_in_mod_p(a, int((t + 1) / 2), P),
                P,
            )
            print("Your Nghiệm : ")
            return r_1, (P - r_1) % P


print("Giải phương trình dạng : x^2 = a (P) ")
while True:
    a = int(input("Nhập giá trị a :"))
    p = int(input("Nhập giá trị p :"))
    print(giai_phuong_trinh_binh_phuong(a, p))
    check = input("You want to continue ?(Y/N)")
    if check == "N":
        break
