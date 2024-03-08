#include <iostream>
#include <cmath>
#include <stdint.h>
#define MAXLEN 10
#define loop(i, a, b) for (int i = a; i < b; i++)
#define I32 int_fast32_t
#define I64 int_fast64_t
#define I8 int_fast8_t
#define N 1739
#define B 7 // cần sửa số B này ////////////////// = e** (1/2 * sqrt(ln(n)lnln(n)))
using namespace std;
I32 FN[] = {-1, 2, 3, 7};
I8 len_FN = 4;
I8 Arr_alpha[MAXLEN];
I32 arr_P[MAXLEN];
void process(I64 D, I64 U, I64 V, I8 n)
{
    long double sqrt_D = sqrt(D);
    I8 P, Q;
    I64 A = int((sqrt_D - U) / V);
    U = U + A * V;
    Arr_alpha[1] = A;
    cout << A << " ";
    arr_P[0] = 1;
    arr_P[1] = A;
    I64 temp;
    I8 count = 0;
    loop(i, 0, n)
    {
        V = (D - U * U) / V;
        A = (sqrt_D + U) / V;
        U = A * V - U;
        Arr_alpha[i + 2] = A;
        arr_P[i + 2] = (arr_P[i + 1] * A + arr_P[i]) % N;
        if (i & 0x1)
        {
            temp = V % N;
            cout << temp << "\n (";
            cout << (temp < 0) << " ";
            loop(j, 1, len_FN)
            {
                count = 0;
                while (temp % FN[j] == 0)
                {
                    count++;
                    temp /= FN[j];
                }
                cout << (count & 0x1) << " ";
            }
            cout << ")\n";
            if (temp != 1 && temp != -1)
                cout << "TH này loại \n";
        }
        else
        {
            temp = -V % N;
            cout << temp << "\n (";
            cout << (temp < 0) << " ";
            loop(j, 1, len_FN)
            {
                count = 0;
                while (temp % FN[j] == 0)
                {
                    count++;
                    temp /= FN[j];
                }
                cout << (count & 0x1) << " ";
            }
            cout << ")\n";
            if (temp != 1 && temp != -1)
                cout << "TH này loại \n";
        }
        // cout << temp << " ";
        cout << A << " ";
        cout << endl;
        cout << arr_P[i + 2] << " ";
    }
    cout << endl;
}

int main()
{
    process(9073, 0, 1, 5);
    return 0;
}