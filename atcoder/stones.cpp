#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k; cin >> n >> k;
    vector<int> a(n), DP(k+1);
    for(int &i : a) cin >> i;
    for(int i : a) DP[i] = 1;
    int l = 0;
    while(!DP[l]) DP[l] = 2;
    for(int i=1; i<=k; i++) {
        if(DP[i]) continue;
        int f = 0;
        for(int j=0; j<n; j++)
            if(i-a[j] > 0 && DP[i-a[j]] == 2)
                f = 1;
        if(f) DP[i] = 1;
        else DP[i] = 2;
    }
    cout << (DP[k] == 1 ? "First" : "Second") << endl;
    return 0;
}
