#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>
#define U64 uint_fast64_t
#define U32 uint_fast32_t
#define U16 uint_fast16_t
#define U8 uint_fast8_t
#define loop(i, a, n) for (U32 i = a; i < n; i++)
#define loopBack(i, n, a) for (int i = n; i >= a; i--)
#define getBitIndex(x, idx) (((x) >> (idx)) & 1)     // get bit tại index
#define setBitIndex(x, idx) ((x) |= (1 << (idx)))    // set bit tại index = 1
#define clearBitIndex(x, idx) ((x) &= ~(1 << (idx))) // clear bit tại index = 0
#define size 5
// số to sau đó số nhỏ
int GCD_u_v(int A, int B, int *u, int *v)
{
    if (A >= B)
    {

        int A0 = A, B0 = B, E = 1, F = 0, G = 0, H = 1, g = 1;
        while ((A0 % 2 == 0) && (B0 % 2 == 0))
        {
            A0 >>= 1;
            B0 >>= 1;
            g <<= 1;
        }
        int x = A0, y = B0;
        while (x)
        {
            while (x % 2 == 0)
            {
                x >>= 1;
                if ((E % 2 == 0) && (F % 2 == 0))
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
                if ((G % 2 == 0) && (H % 2 == 0))
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
        int d = g * y;
        if (A * G + B * H == d)
        {
            *u = G;
            *v = H;
        }
        else
        {
            *u = -G;
            *v = -H;
        }
        printf("d = %d, u = %d , v = %d\n", d, *u, *v);
        return d;
    }
    else
    {
        return GCD_u_v(B, A, v, u);
    }
}
int LOG2(int x)
{
    int result = -1;
    while (x != 0)
    {
        result++;
        x >>= 1;
    }
    return result;
}
void transformFourier(U32 vec_A[], U32 omega, U32 len_bit, U32 Mod)
{
    U32 log_n = LOG2(len_bit);
    U32 vec_omg[len_bit];
    U32 v_a_cp[len_bit];
    U8 array_index[len_bit];
    array_index[0] = 0;
    loop(i, 0, len_bit)
    {
        v_a_cp[i] = vec_A[i];
    }
    vec_omg[0] = 1;
    // vec_omg[1] = omega;
    U32 part_num, len_part, len_halfpart, len_current_omg = 1, po_omg;
    loop(turn, 0, log_n)
    {
        part_num = 1 << turn;
        len_part = len_bit / part_num;
        len_halfpart = len_part >> 1;
        po_omg = pow(omega, len_bit >> (turn + 1));
        po_omg %= Mod;

        // tao moi omega cho luot sau
        loop(idx3, 0, len_current_omg)
        {
            vec_omg[idx3 + len_current_omg] = (vec_omg[idx3] * po_omg) % Mod;
            array_index[idx3 + len_current_omg] = array_index[idx3] + (len_bit >> (turn + 1));
        }
        len_current_omg <<= 1;

        loop(part, 0, part_num)
        {
            loop(idx1, 0, len_halfpart)
            {
                v_a_cp[part * len_part + idx1] = (vec_A[part * len_part + idx1] + vec_A[part * len_part + idx1 + len_halfpart] * vec_omg[(part << 1)]) % Mod;
            }
            // nura sau
            loop(idx2, 0, len_halfpart)
            {
                v_a_cp[part * len_part + idx2 + len_halfpart] = (vec_A[part * len_part + idx2] + vec_A[part * len_part + idx2 + len_halfpart] * vec_omg[(part << 1) + 1]) % Mod;
            }
        }

        loop(i, 0, len_bit)
        {
            vec_A[i] = v_a_cp[i];
            printf("arr[%i] = %d  ", i, v_a_cp[i]);
        }
        printf("\n");
        // tao moi omega cho luot sau
        // loop(idx3, 0, len_current_omg)
        // {
        //     vec_omg[idx3 + len_current_omg] = (vec_omg[idx3] * omega) % Mod;
        // }
    }
    loop(i, 0, len_bit)
    {
        vec_A[array_index[i]] = v_a_cp[i];
    }
    // sap xep lai mang theo dung index
    loop(i, 0, len_bit)
        printf("arr[%i] = %d  ", i, vec_A[i]);
    printf("\n");
}
void inverseTransformFourier(U32 vec_A[], U32 omega, U32 len_bit, U32 Mod)
{
    U32 log_n = LOG2(len_bit);
    U32 vec_omg[len_bit];
    U32 v_a_cp[len_bit];
    U8 array_index[len_bit];
    array_index[0] = 0;
    loop(i, 0, len_bit)
    {
        v_a_cp[i] = vec_A[i];
    }
    vec_omg[0] = 1;
    // vec_omg[1] = omega;
    U32 part_num, len_part, len_halfpart, len_current_omg = 1, po_omg;
    loop(turn, 0, log_n)
    {
        part_num = 1 << turn;
        len_part = len_bit / part_num;
        len_halfpart = len_part >> 1;
        po_omg = pow(omega, len_bit >> (turn + 1));
        po_omg %= Mod;

        // tao moi omega cho luot sau
        loop(idx3, 0, len_current_omg)
        {
            vec_omg[idx3 + len_current_omg] = (vec_omg[idx3] * po_omg) % Mod;
            array_index[idx3 + len_current_omg] = array_index[idx3] + (len_bit >> (turn + 1));
        }
        len_current_omg <<= 1;

        loop(part, 0, part_num)
        {
            loop(idx1, 0, len_halfpart)
            {
                v_a_cp[part * len_part + idx1] = (vec_A[part * len_part + idx1] + vec_A[part * len_part + idx1 + len_halfpart] * vec_omg[(part << 1)]) % Mod;
            }
            // nura sau
            loop(idx2, 0, len_halfpart)
            {
                v_a_cp[part * len_part + idx2 + len_halfpart] = (vec_A[part * len_part + idx2] + vec_A[part * len_part + idx2 + len_halfpart] * vec_omg[(part << 1) + 1]) % Mod;
            }
        }

        loop(i, 0, len_bit)
        {
            vec_A[i] = v_a_cp[i];
            printf("arr[%i] = %d  ", i, v_a_cp[i]);
        }
        printf("\n");
        // tao moi omega cho luot sau
        // loop(idx3, 0, len_current_omg)
        // {
        //     vec_omg[idx3 + len_current_omg] = (vec_omg[idx3] * omega) % Mod;
        // }
    }
    // tìm nghịch dảo của n
    int u, v;
    GCD_u_v(Mod, len_bit, &u, &v);
    U32 invertElem = (v + Mod) % Mod;
    // sap xep lai mang theo dung index
    loop(i, 0, len_bit)
    {
        vec_A[array_index[i]] = v_a_cp[i];
    }
    // đảo nguojc lại mảng a

    len_halfpart = len_bit >> 1;
    loop(idx, 1, len_halfpart)
    {
        po_omg = (vec_A[idx] * invertElem) % Mod;
        vec_A[idx] = (vec_A[len_bit - idx] * invertElem) % Mod;
        vec_A[len_bit - idx] = po_omg;
    }
    vec_A[len_halfpart] = (vec_A[len_halfpart] * invertElem) % Mod;
    vec_A[0] = (vec_A[0] * invertElem) % Mod;
    loop(i, 0, len_bit)
        printf("arr[%i] = %d  ", i, vec_A[i]);
    printf("\n");
}
U32 findInvertElem(U32 elem, U32 Mod)
{
    int u, v;
    GCD_u_v(Mod, elem, &u, &v);
    return ((v + Mod) % Mod);
}
void multiplyPolynomial(U32 F_x[], U32 G_x[], U32 deg_f, U32 deg_g, U32 Mod, U32 omega)
{
    U32 deg_sum = deg_f + deg_g;
    U32 len_bit = 1;
    // w
    while (deg_sum + 1 > len_bit)
        len_bit <<= 1;
    // lap day vec f va g
    U32 *vec_A;
    vec_A = (U32 *)malloc(len_bit * sizeof(U32));
    U32 vec_B[len_bit];
    loop(idx, 0, deg_f + 1)
        vec_A[idx] = F_x[idx];
    loop(idx, 0, deg_g + 1)
        vec_B[idx] = G_x[idx];
    loop(idx, deg_f + 1, len_bit)
        vec_A[idx] = 0;
    loop(idx, deg_g + 1, len_bit)
        vec_B[idx] = 0;
    transformFourier(vec_A, omega, len_bit, Mod);
    transformFourier(vec_B, omega, len_bit, Mod);
    loop(idx, 0, len_bit)
    {
        vec_A[idx] = (vec_A[idx] * vec_B[idx]) % Mod;
    }
    inverseTransformFourier(vec_A, omega, len_bit, Mod);
    loop(idx, deg_f + 1, len_bit)
        F_x[idx] = vec_A[idx];
    free(vec_A);
    // return vec_A;
}

void reverseKoefficients(U32 F_x[], U32 len_f)
{
    U32 temp;
    loop(idx, 0, len_f >> 1)
    {
        temp = F_x[idx];
        F_x[idx] = F_x[len_f - 1 - idx];
        F_x[len_f - 1 - idx] = temp;
    }
}
void subtractPolynomial(U32 F[], U32 G[], U32 len, U32 Mod)
{
    loop(idx, 0, len)
    {
        F[idx] = (F[idx] - G[idx] + Mod) % Mod;
    }
}
void changePolynominal(U32 P[], U32 G[], U32 deg, U32 Mod)
{
    U32 *res;
    U32 P_cp[deg + 1];
    loop(idx, 0, deg + 1)
        P_cp[idx] = (2 * P[idx]) % Mod;
    multiplyPolynomial(P, P, deg, deg, Mod, 2);
    multiplyPolynomial(P, G, deg, deg, Mod, 2);
    subtractPolynomial(P_cp, P, deg + 1, Mod);
}
void dividePolynomial(U32 F[], U32 G[], U32 deg_f, U32 deg_g, U32 Mod)
{
    U32 k = LOG2(deg_f - deg_g) + 1;
    reverseKoefficients(F, deg_f + 1);
    U32 inverLeadCoeffG = findInvertElem(G[deg_g], Mod);
    reverseKoefficients(G, deg_g + 1);
    U32 P[deg_f + 1];
    U32 F_temp[deg_f + 1];
    loop(i, 0, deg_f + 1)
        F_temp[i] = F[i];
    U32 P_temp[deg_f + 1];
    loop(i, 0, deg_f + 1)
        P[i] = 0;
    P[0] = inverLeadCoeffG;
    loop(i, 1, k)
    {
        changePolynominal(P, G, deg_f, Mod);
        loop(i, 0, deg_f + 1)
            printf("F[%d] = %d    ", i, P[i]);
        printf("\n");
    }
    // loop(i, 0, 4)
    //     printf("F[%d] = %d      ", i, F[i]);
    // printf("\n");
    // loop(i, 0, 4)
    //     printf("P[%d] = %d      ", i, P[i]);
    // printf("\n");
    multiplyPolynomial(F, P, deg_f, deg_f, Mod, 2);
    // loop(i, 0, deg_f + 1)
    //     printf("F[%d] = %d      ", i, F[i]);
    // printf("\n");
    // lay he so den (x ^ (n-m))
    loop(idx, 0, deg_f - deg_g + 1)
    {
        P[idx] = F[idx];
        P_temp[idx] = F[idx];
    }
    loop(idx, deg_f - deg_g + 1, deg_f + 1)
    {
        P[idx] = 0;
        P_temp[idx] = 0;
    }
    // dao nguoc lai P
    reverseKoefficients(P, deg_f - deg_g + 1);
    // loop(i, 0, deg_f + 1)
    //     printf("P[%d] = %d      ", i, P[i]);
    // printf("\n");
    // nhan P' va G'
    multiplyPolynomial(P_temp, G, deg_f - deg_g, deg_g, Mod, 2);
    // loop(i, 0, deg_f + 1)
    //     printf("P[%d] = %d      ", i, P_temp[i]);
    // printf("\n");
    subtractPolynomial(F_temp, P_temp, deg_f + 1, Mod);
    // loop(i, 0, deg_f + 1)
    //     printf("P[%d] = %d      ", i, F_temp[i]);
    // printf("\n");
    reverseKoefficients(F_temp, deg_f + 1);
}

int main()
{
    // U32 vec_A[5] = {1, 3, 2, 0, 1};
    U32 F[] = {1, 1, 0, 2};
    U32 G[] = {1, 0, 1, 0};
    U32 len_f = 3;
    U32 len_g = 2;
    U32 Mod = 5;
    dividePolynomial(F, G, len_f, len_g, Mod);
    return 0;
}