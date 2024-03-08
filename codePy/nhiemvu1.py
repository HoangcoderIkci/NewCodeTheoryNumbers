import math
import numpy as np


# Mang_phep_cong = []
# Mang_phep_nhan = []
# Mang_doi_cong = []
# Mang_nghich_dao = []
# Mang_phep_tru = []
# Character_Pole = int(input("Character pole: "))
def Nhan_trong_module(A, B, Module):
    n = math.ceil(math.log(Module, 2))
    C = 2 ** (2 * n)
    R = 0
    for i in range(n):
        if A & 0b01:
            R += B
        if R & 0b01:
            R += Module
        R >>= 1
        A >>= 1
    if R >= Module:
        R -= Module
        A, B = R, C
        R = 0
    for i in range(n):
        if A & 0b01:
            R += B
        if R & 0b01:
            R += Module
        R >>= 1
        A >>= 1
    if R >= Module:
        R -= Module
    return R


Character_Pole = 3


def init_all_arrays():
    Mang_phep_cong = [[0 for j in range(Character_Pole)] for i in range(Character_Pole)]
    Mang_phep_nhan = [[0 for j in range(Character_Pole)] for i in range(Character_Pole)]
    Mang_phep_tru = [[0 for j in range(Character_Pole)] for i in range(Character_Pole)]
    Mang_phep_chia = [[0 for j in range(Character_Pole)] for i in range(Character_Pole)]
    Mang_nghich_dao = [0] * Character_Pole
    Mang_doi_cong = [0] * Character_Pole
    temp1 = 0
    temp2 = 0
    for i in range(1, Character_Pole):
        Mang_doi_cong[i] = Character_Pole - i
    Mang_doi_cong[0] = 0
    # create Mang_phep_cong
    for i in range(Character_Pole):
        for j in range(i, Character_Pole):
            temp1 = (i + j) % Character_Pole
            Mang_phep_cong[i][j] = temp1
            Mang_phep_cong[j][i] = temp1
            temp2 = Nhan_trong_module(i, j, Character_Pole)
            temp2 = (i * j) % Character_Pole
            Mang_phep_nhan[i][j] = temp2
            Mang_phep_nhan[j][i] = temp2
            if temp2 == 1:
                Mang_nghich_dao[i] = j
                Mang_nghich_dao[j] = i
    for i in range(Character_Pole):
        Mang_phep_tru[i][0] = i
        for j in range(1, Character_Pole):
            Mang_phep_tru[i][j] = Mang_phep_cong[i][Mang_doi_cong[j]]
            Mang_phep_chia[i][j] = Mang_phep_nhan[i][Mang_nghich_dao[j]]
    return (
        Mang_phep_cong,
        Mang_phep_nhan,
        Mang_doi_cong,
        Mang_nghich_dao,
        Mang_phep_tru,
        Mang_phep_chia,
    )


(
    Mang_phep_cong,
    Mang_phep_nhan,
    Mang_doi_cong,
    Mang_nghich_dao,
    Mang_phep_tru,
    Mang_phep_chia,
) = init_all_arrays()
# print("+: Mang_phep_cong")
# print(Mang_nghich_dao)
# print("*")
# print(Mang_phep_tru)
# print(Mang_phep_chia)


def tim_vi_tri_dau_tien_khac_0(lst):
    for i, x in enumerate(lst):
        if x != 0:
            return i
    return -1


def cong_polies(Expr1, Expr2):
    l1 = len(Expr1)
    l2 = len(Expr2)
    if l1 < l2:
        do_chech = l2 - l1
        res = Expr2.copy()
        for k in range(l1):
            res[k + do_chech] = Mang_phep_cong[res[k + do_chech]][Expr1[k]]
    else:
        res = Expr1.copy()
        do_chech = l1 - l2
        for k in range(l2):
            res[k + do_chech] = Mang_phep_cong[res[k + do_chech]][Expr2[k]]
    return res


def poly_divide(poly1, poly2):
    """
    Chia dư 2 đa thức poly1 và poly2.
    Trả về kết quả là đa thức thương và đa thức dư.
    """
    # Kiểm tra nếu poly2 là đa thức bậc 0 và hệ số khác 0
    if all(x == 0 for x in poly2):
        return 9999999999999

    p1_cp = []
    k = 0
    while poly1[k] == 0:
        k += 1
    p1_cp = poly1[k:]
    p2_cp = []
    k = 0
    while poly2[k] == 0:
        k += 1
    p2_cp = poly2[k:]
    do_lech = len(p1_cp) - len(p2_cp)
    if do_lech < 0:
        return np.array([0]), p1_cp
    if len(p2_cp) == 1:
        return p1_cp, np.array([0])
    vi_tri_khac_0 = tim_vi_tri_dau_tien_khac_0(p1_cp)
    hs = 0
    hs_chia_max = p2_cp[0]

    # p2_cp = np.pad(p2_cp, (0, do_lech), mode="constant")
    thuong = []
    while vi_tri_khac_0 <= do_lech:
        hs = Mang_phep_chia[p1_cp[vi_tri_khac_0]][hs_chia_max]
        thuong.append(hs)
        for t in range(len(p2_cp)):
            p1_cp[vi_tri_khac_0 + t] = Mang_phep_tru[p1_cp[vi_tri_khac_0 + t]][
                Mang_phep_nhan[p2_cp[t]][hs]
            ]
        vi_tri_khac_0 = tim_vi_tri_dau_tien_khac_0(p1_cp)
    k = 0
    while p1_cp[k] == 0:
        k += 1
    thuong = thuong + [0] * (do_lech - len(thuong))
    return np.array(thuong), p1_cp[k:]


def multPoly(poly1, poly2):
    l1 = len(poly1)
    l2 = len(poly2)
    l_res = l1 + l2 - 1
    res = [0] * (l_res)
    for i in range(l2):
        if poly2[i] != 0:
            for j in range(l1):
                a = Mang_phep_nhan[poly1[j]][poly2[i]]
                res[i + j] = Mang_phep_cong[res[i + j]][a]
    k = 0
    while res[k] == 0:
        k += 1
    return np.array(res[k:])


def gcd_poly(poly1, poly2):
    p1_cp = poly1.copy()
    p2_cp = poly2.copy()
    if np.all(p2_cp == 0):
        return p1_cp
    while True:
        temp = poly_divide(p1_cp, p2_cp)[1]
        if np.all(temp == 0):
            return p2_cp
        p1_cp = p2_cp
        p2_cp = temp


def tim_nghiem_so_sanh(a, b, Mod):
    a, b = a % Mod, b % Mod
    if a % Mod == 0:
        if b % Mod == 0:
            return [i for i in range(Mod)]
        else:
            return -9999
    return Mang_phep_chia[b][a]


# d


def calcValueMod(Expr, x):
    res = Expr[0]
    for a in range(len(Expr) - 1):
        res = Mang_phep_cong[Mang_phep_nhan[res][x]][Expr[a + 1]]
    return res


def thuat_toan_thuc_giac(Expr_poly, so_mu, nghiem, Mod):
    nghiem = nghiem % Mod
    poly_f1 = np.array(Expr_poly)
    dpolydx = np.polyder(poly_f1)
    coeffs = dpolydx.tolist()
    gia_tri_plder = calcValueMod(coeffs, nghiem)
    vector_a = [nghiem]
    b = 0
    for i in range(so_mu - 1):
        b += (Mod**i) * vector_a[i]
        gia_tri_ply = calcValueMod(Expr_poly, b)
        vector_a.append(
            tim_nghiem_so_sanh(gia_tri_plder, int(-gia_tri_ply / (Mod ** (i + 1))), Mod)
        )
    return vector_a


def check_dieu_kien_1(Expr_poly):
    poly_goc = np.array(Expr_poly)
    dpolydx = np.polyder(poly_goc) % 2
    gcdPoly = gcd_poly(poly_goc, dpolydx)
    coeffs = gcdPoly.tolist()
    k = 0
    while coeffs[k] == 0:
        k += 1
    coeffs = coeffs[k:]
    if coeffs[0] != 1 or len(coeffs) != 1:
        return False
    return True


def kiem_tra_bat_kha_quy(Expr_poly):
    if check_dieu_kien_1(Expr_poly):
        n = len(Expr_poly) - 1
        list_coeffs_C = [[0] * n]
        for i in range(1, n):
            temp = [0] * (Character_Pole * i + 1)
            temp[0] = 1
            temp[-i - 1] = Character_Pole - 1
            C_i = poly_divide(np.array(temp), np.array(Expr_poly))[1]
            coeff_C_i = C_i.tolist()
            do_lech = n - len(coeff_C_i)
            if do_lech:
                coeff_C_i = [0] * do_lech + coeff_C_i
            list_coeffs_C.append(coeff_C_i)
        print("Matrix C: ")
        print(np.array(list_coeffs_C))
        rank_A = np.linalg.matrix_rank(np.array(list_coeffs_C))
        if rank_A == n - 1:
            print("da thuc bat kha quy tren poly ", Character_Pole)
        else:
            print(
                "da thuc khong bat kha quy tren poly ( khong thoa man dkien 2) Z",
                Character_Pole,
            )
    else:
        print(
            "da thuc khong bat kha quy tren poly ( khong thoa man dkien 1) Z",
            Character_Pole,
        )


def chinese_function(VectorA, VectorB):
    len_vec = len(VectorA)
    set_A = set(VectorA)
    if len_vec != len(VectorB) or len_vec != len(set_A):
        return -99999
    m_x = [1]
    h_x = [VectorB[0]]
    for i in range(0, len_vec - 1):
        m_x = list(
            multPoly(np.array(m_x), np.array([1, (-VectorA[i]) % Character_Pole]))
        )
        c = Mang_nghich_dao[calcValueMod(m_x, VectorA[i + 1])]
        q = Mang_phep_nhan[
            Mang_phep_tru[VectorB[i + 1]][calcValueMod(h_x, VectorA[i + 1])]
        ][c]
        temp = list(multPoly(np.array([q]), np.array(m_x)))
        h_x = cong_polies(h_x, temp)
    print(h_x)
    return h_x


#

# poly = np.array([1, 2, 1, 1])
# dpolydx = np.polyder(poly)
# print(dpolydx)

# poly1 = np.array([1, 1, 1])  # Đa thức bị chia
# poly2 = np.array([1, 1])  # Đa thức chia
# # print(gcd_poly(poly1, poly2))
# # print(calcValueMod([1, 4, -3, 2], 2))
# # print(thuat_toan_thuc_giac([1, 7, 10, 16], 3, 2, 3))
# kiem_tra_bat_kha_quy([1, 1, 0, 1])
init_all_arrays()
# print(calcValueMod([1, 2, 2], 1))

# print(cong_polies([1, 0], [2, 2, 1]))
chinese_function([1, 2, 0], [0, 1, 1])
