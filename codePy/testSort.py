import numpy as np

# # Chia đa thức x^3 + 2x^2 - 5x + 6 cho đa thức x - 2
poly1 = np.array([1, 4, 2, 1])  # Đa thức bị chia
poly2 = np.array([1, 1, 1])  # Đa thức chia


def tim_vi_tri_dau_tien_khac_0(lst):
    for i, x in enumerate(lst):
        if x != 0:
            return i
    return -1


# result = np.polydiv(poly1, poly2)
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
        return p1_cp
    vi_tri_khac_0 = tim_vi_tri_dau_tien_khac_0(p1_cp)
    hs = 0
    hs_chia_max = p2_cp[0]

    # p2_cp = np.pad(p2_cp, (0, do_lech), mode="constant")

    while vi_tri_khac_0 <= do_lech:
        hs = bang p1_cp[vi_tri_khac_0] / hs_chia_max
        for t in range(len(p2_cp)):
            p1_cp[vi_tri_khac_0 + t] -= p2_cp[t] * hs
        vi_tri_khac_0 = tim_vi_tri_dau_tien_khac_0(p1_cp)
    k = 0
    while p1_cp[k] == 0:
        k += 1
    return p1_cp[k:]
    # for i in poly2:
    #     if i != 0:
    #         p2_cp.append(i)
    # p1_copy = (poly1).copy()
    # p2_copy = (poly2).copy()


# # In kết quả
# print("Thương: ", result[0])  # Thương: [1. 4. 3.]
# print("Dư: ", result[1])  # Dư: [8.]
def gcd_poly(poly1, poly2):
    if np.all(poly2 == 0):
        return poly1
    phan_du = np.polydiv(poly1, poly2)[1]
    return gcd_poly(poly2, phan_du)


# print(polydiv(poly1, poly2))
print(poly_divide(poly1, poly2))
print(np.polydiv(poly1, poly2))
