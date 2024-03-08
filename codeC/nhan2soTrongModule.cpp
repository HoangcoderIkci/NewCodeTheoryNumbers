#include <iostream>
#include <stdint.h>
#define U32 int_fast32_t
#define U64 int_fast64_t
#define U8 int_fast8_t
#define getBit(A, len_bit) (A & ((1 << (len_bit)) - 1))
using namespace std;
U8 lenBit(U64 x)
{
    U8 count = 0;
    while (x != 0)
    {
        ++count;
        x >>= 1;
    }
    return count;
}
U64 multiply(U64 A, U64 B)
{
    int flag = 1;
    U8 len_bit_A = lenBit(A);
    U8 len_bit_B = lenBit(B);
    U8 len_bit = len_bit_A > len_bit_B ? len_bit_A : len_bit_B;
    if (A < 0)
    {
        A = -A;
        flag *= -1;
    }
    if (B < 0)
    {
        B = -B;
        flag *= -1;
    }
    if (len_bit > 1)
    {
        len_bit >>= 1;
        // U64 A_0 = A & ((1 << (len_bit)) - 1);
        U64 A_0 = getBit(A, len_bit);
        U64 A_1 = A >> len_bit;
        U64 B_0 = getBit(B, len_bit);
        U64 B_1 = B >> len_bit;
        U64 res;
        U64 temp1, temp2, temp3;
        temp1 = multiply(A_1, B_1);
        temp2 = multiply(A_0, B_0);
        temp3 = multiply(A_0 - A_1, B_1 - B_0);
        res = (temp1 << (2 * len_bit)) + (temp1 << len_bit) + (temp3 << len_bit) + (temp2 << len_bit) + temp2;
        return res * flag;
    }
    return (A & B) * flag;
}

U64 supportPower(U64 A, U8 len_bit)
{
    if (A < 0)
    {
        A = -A;
    }
    if (len_bit > 1)
    {
        len_bit >>= 1;
        // U64 A_0 = A & ((1 << (len_bit)) - 1);
        U64 A_0 = getBit(A, len_bit);
        U64 A_1 = A >> len_bit;
        // U64 B_0 = getBit(B, len_bit);
        // U64 B_1 = B >> len_bit;
        U64 res;
        U64 temp1, temp2, temp3;
        temp1 = supportPower(A_1, len_bit);
        temp2 = supportPower(A_0, len_bit);
        temp3 = -supportPower(A_1 - A_0, len_bit);
        res = (temp1 << (2 * len_bit)) + (temp1 << len_bit) + (temp3 << len_bit) + (temp2 << len_bit) + temp2;
        return res;
    }
    return A;
}
U64 power(U64 A, U64 B, U8 len_bit)
{
    U64 res;
    if (B & 0b1)
        res = A;
    else
        res = 1;
    B >>= 1;
    while (B)
    {
        A = supportPower(A, len_bit);
        len_bit *= 2;
        if (B & 0b1)
            res = multiply(A, res);
        B >>= 1;
    }
    return res;
}
// số to sau đó số nhỏ
U32 GCD_u_v(U32 A, U32 B, U32 &u, U32 &v)
{
    if (A >= B)
    {

        U32 A0 = A, B0 = B, E = 1, F = 0, G = 0, H = 1, g = 1;
        while ((!(A0 & 0b1)) && (!(B0 & 0b1)))
        {
            A0 >>= 1;
            B0 >>= 1;
            g <<= 1;
        }
        U32 x = A0, y = B0;
        while (x)
        {
            while (x % 2 == 0)
            {
                x >>= 1;
                if ((!(E & 0b1)) && (!(F & 0b1)))
                {
                    E >>= 1;
                    F >>= 1;
                }
                else
                {
                    E = (E + B0) >> 1;
                    F = (F - A0) >> 1;
                }
            }
            while (y % 2 == 0)
            {
                y >>= 1;
                if ((!(G & 0b1)) && (!(H & 0b1)))
                {
                    G >>= 1;
                    H >>= 1;
                }
                else
                {
                    G = (G + B0) >> 1;
                    H = (H - A0) >> 1;
                }
            }
            if (x >= y)
            {
                x -= y;
                E -= G;
                F -= H;
            }
            else
            {
                y -= x;
                G -= E;
                H -= F;
            }
        }
        U32 d = g * y;
        if (A * G + B * H == d)
        {
            u = G;
            v = H;
        }
        else
        {
            u = -G;
            v = -H;
        }
        cout << "d = " << d << endl;
        cout << "u = " << u << endl;
        cout << "v = " << v << endl;
        return d;
    }
    else
    {
        return GCD_u_v(B, A, v, u);
    }
}

// chỉ dành cho số lẻ Module
U64 multiplyWithModule(U64 A, U64 B, U64 M)
{
    U8 bit_len = lenBit(M);
    U64 C = (1 << (2 * bit_len)) % M;
    U64 R = 0;
    for (int i = 0; i < bit_len; i++)
    {
        if (A & 0b1)
            R += B;
        if (R & 0b1)
            R += M;
        R >>= 1;
        A >>= 1;
    }
    if (R >= M)
        R -= M;
    A = R;
    B = C;
    R = 0;
    for (int i = 0; i < bit_len; i++)
    {
        if (A & 0b1)
            R += B;
        if (R & 0b1)
            R += M;
        R >>= 1;
        A >>= 1;
    }
    return R;
}

// Giải hệ so sánh module
// cần mảng đầu vào arrM : factor của M. arrU tương úng so sánh u1,u2,...,uk
// Đặc biệt m lẻ do bên trong dùng hàm nhân module với Module lẻ.
U32 solveSystemModule(U32 arrM[], U32 arrU[], U8 k)
{
    U64 M = 1;
    for (int i = 0; i < k; i++)
    {
        M *= arrM[i];
    }
    U32 u = 0, v = 0, c, d;
    for (int i = 0; i < k; i++)
    {
        c = M / arrM[i];
        GCD_u_v(c, arrM[i], d, v);
        d = (d + arrM[i]) % arrM[i];
        u += multiplyWithModule(c, multiplyWithModule(d, arrU[i], M), M);
    }
    return u;
}
U32 solveSystemModule2(U32 arrM[], U32 arrU[], U8 k)
{
    U64 M = 1;
    for (int i = 0; i < k; i++)
    {
        M *= arrM[i];
    }
    U32 u = 0, v = 0, c, d;
    for (int i = 0; i < k; i++)
    {
        c = M / arrM[i];
        GCD_u_v(c, arrM[i], d, v);
        d = (d + arrM[i]) % arrM[i];
        u += c * d * arrU[i];
        u %= M;
        // u += multiplyWithModule(c, multiplyWithModule(d, arrU[i], M), M);
    }
    return u;
}

U64 calcValOfFucInPoint(U32 arrHs[], U32 x)
{
    U8 len = sizeof(arrHs) / sizeof(arrHs[0]);
    U64 res = 1;
    for (int i = len - 1; i >= 0; i--)
    {
        res = multiply(res, arrHs[i]) + x;
    }
    return res;
}
int main()
{
    U32 arrM[] = {9, 5, 4};
    U32 arrU[] = {7, 4, 2};
    auto res = solveSystemModule2(arrM, arrU, 3);
    printf("res = %d\n", res);
    // cout << calcValOfFucInPoint(arrHs, x);
    return 0;
}