#include <iostream>
#include <math.h>
#include <stdio.h>
using namespace std;

int main() {
    double n, m, a = 0;
    cin >> n >> m >> a;
    printf("%llu", (long long unsigned int)(ceil(n/a)*ceil(m/a)));
}
