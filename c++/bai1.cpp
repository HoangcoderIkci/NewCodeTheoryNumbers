#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;
#define SIZEPOLE 16
#define CHAR 2
#define DEGREE 4
#define hsPole 19

unsigned arrMultiple[SIZEPOLE][SIZEPOLE];
unsigned arrInverseSubtraction[SIZEPOLE];

unsigned multipleTwoElement(unsigned a, unsigned b)
{
    if (a == 0 || b == 0)
        return 0;
    unsigned result = 0;
    unsigned temp = 1 << DEGREE;
    unsigned a_cp = 0;
    int k = 0, t;
    while (b != 0)
    {
        if (b & 0x1)
        {
            t = k;
            a_cp = a;
            while (t)
            {
                a_cp <<= 1;
                t--;
                if (a_cp & temp)
                {
                    a_cp ^= hsPole;
                }
            }
            result ^= a_cp;
        }
        k++;
        b >>= 1;
    }
    return result;
}
void createArrayMult()
{
    unsigned temp = 0;
    for (unsigned i = 0; i < SIZEPOLE; i++)
    {
        for (unsigned j = i; j < SIZEPOLE; j++)
        {
            temp = multipleTwoElement(i, j);
            // cout << i << "*" << j << " = " << temp << endl;
            arrMultiple[i][j] = temp;
            arrMultiple[j][i] = temp;
            if (temp == 1)
            {
                arrInverseSubtraction[i] = j;
                arrInverseSubtraction[j] = i;
            }
        }
    }
}
void __INIT_FIELD()
{
    createArrayMult();
}
int main()
{
    vector<vector<int>> result;
    vector<int> s2 = {1, 2, 3};
    result.push_back(s2);
    cout << result[0][1] << endl;
    return 0;
}