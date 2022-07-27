#include <iostream>
using namespace std;

int zeros(int scores[], int k) {
    int zs=0;
    for(int i=0; i<k; i++) if(scores[i]==0) ++zs;
    return zs;
}

int main() {
    int n, k; cin >> n >> k;
    int scores[n];
    for(int i=0; i<n; i++) cin >> scores[i];
    if(n==k) cout << k-zeros(scores, k);
    else {
        int a=0;
        int zeroes=0;
        for(int i=k; i<n; i++) {
            if(scores[i]<=0) break;
            if(scores[k-1]!=scores[i]) break;
            else ++a;
        }
        cout << (k+a)-zeros(scores, k);
    }
}
