#include <bits/stdc++.h>
using namespace std;

int MAXN = 10001;

int main() {
    int n; cin >> n;
    vector<int> nums(n), DP(MAXN);
    DP[0] = 1;
    for(int i=0; i<n; i++) cin >> nums[i];
    for(int i=0; i<n; i++) {
        int val = nums[i];
        for(int j=MAXN; j>=val; j--)
            if(DP[j-val])
                DP[j] = 1;
    }
    for(int i=0; i<1001; i++) {
        if(DP[1000+i]) {
            cout << 1000+i << endl;
            break;
        }
        if(DP[1000-i]) {
            cout << 1000-i << endl;
            break;
        }
    }
    return 0;
}
