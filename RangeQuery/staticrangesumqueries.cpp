#include <iostream>
using namespace std;

typedef long long ll;

int main() {
    ll n,q; cin >> n >> q;
    ll x[n+1];
    for(int i=1; i<=n; i++) {
        cin >> x[i];
        x[i] += x[i-1];
    }
    for(int i=0; i<q; i++) {
        int a,b; cin >> a >> b;
        cout << x[b]-x[a-1] << endl;
    }
}
