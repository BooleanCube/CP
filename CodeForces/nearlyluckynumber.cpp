#include <iostream>
using namespace std;

int main() {
    long long num; cin >> num;
    int c=0;
    while(num > 0) { if(num%10==4 || num%10==7) ++c; num/=10; }
    if(c==4 || c==7) cout << "YES";
    else cout << "NO";
}
