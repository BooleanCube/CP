#include <bits/stdc++.h>
using namespace std;

vector<int> mnseg, mxseg;

int minquery(int l, int r, int mn) {
    if(l == r) return min(mn, mnseg[l]);
    if((l & 1) == 1) return minquery(l+1, r, min(mn, mnseg[l]));
    if((r & 1) == 0) return minquery(l, r-1, min(mn, mnseg[r]));
    return minquery((l >> 1), (r >> 1), mn);
}

int minupdate(int idx, int val) {
    while(idx > 0) {
        mnseg[idx] = val;
        idx >>= 1;
    }
}

int maxquery(int l, int r, int mx) {
    if(l == r) return max(mx, mnseg[l]);
    if((l & 1) == 1) return maxquery(l+1, r, max(mx, mnseg[l]));
    if((r & 1) == 0) return maxquery(l, r-1, max(mx, mnseg[r]));
    return maxquery((l >> 1), (r >> 1), mx);
}

int maxupdate(int idx, int val) {
    while(idx > 0) {
        mxseg[idx] = val;
        idx >>= 1;
    }
}

int main() {
    int n, m; cin >> n >> m;
    vector<int> nums(n);
    for(int i=0; i<n; i++) cin >> nums[i];
    mnseg = vector<int>(2*n);
    mxseg = vector<int>(2*n);
    
    return 0;
}