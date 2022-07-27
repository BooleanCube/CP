#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int i=1, j=0;
    int sum;
    for(int k=0; k<25; k++) {
        ++j; if(j>5){j=1;++i;}
        int l; cin >> l;
        if(l == 1) sum = abs(i-3) + abs(j-3);
    }
    cout << sum;
    return 0;
}
