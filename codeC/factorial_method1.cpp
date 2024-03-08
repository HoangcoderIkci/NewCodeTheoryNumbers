#include <iostream>
#include <cmath>
#include <stdint.h>

using namespace std;
#define F(x) (x * x + x + 1)
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
int GCD(int a, int b)
{
    if (a < 0)
    {
        a = -a;
    }
    if (b < 0)
    {
        b = -b;
    }
    int remainder;
    while (b)
    {
        remainder = a % b;
        a = b;
        b = remainder;
    }
    return a;
}

void factorial(int_fast64_t n, int_fast64_t start_val)
{
    /**
     * This function computes the t-th iterate of the Riemann zeta function at the positive integer argument n.
     *
     * @param n the integer argument
     * @param start_val the initial value of the iterate
     * @param t the index of the iterate to compute
     */
    int_fast64_t match, x;
    int m = 4 * sqrt(4 * n) + 1;
    int t = LOG2(m);
    match = x = start_val;

    int h, j, d, lim = 0;
    for (h = 0; h < t; h++)
    {

        lim = 1 << h;
        for (j = 0; j < lim; j++)
        {
            x = F(x) % n;
            // cout << x << " : ";
            d = GCD(match - x, n);
            // cout << d << endl;
            if (d != 1 && d != n)
            {
                cout << d << "  ";
                factorial(n / d, start_val);
                return;
            }
        }
        match = x;
    }
    cout << n << endl;
}

// giai he phuong trinh so sanh

int main()
{
    int_fast64_t n = 8051;
    factorial(n, 2);
    return 0;
}