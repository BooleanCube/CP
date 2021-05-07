//accepted
//watch out for scientific notation, wouldnt be a problem if you were solving with python.

#include <iostream>
#include <math.h>
#include <stdio.h>
using namespace std;

int main() {
    double n, m, a = 0;
    cin >> n >> m >> a;
    printf("%llu", (long long unsigned int)(ceil(n/a)*ceil(m/a)));
}
