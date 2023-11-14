#include <bits/stdc++.h>
using namespace std;

vector<int> tree;

void update(int idx, int val=1) {
    while(idx > 0) {
        tree[idx] += val;
        idx >>= 1;
    }
}

int query(int l, int r, int s) {
    if(l == r) return s+tree[l];
    if((l&1) == 1) return query(l+1, r, s+tree[l]);
    if((r&1) == 0) return query(l, r-1, s+tree[r]);
    return query(l>>1, r>>1, s);
}

int main() {
    int n; cin >> n;
    tree = vector<int>(2*n);
    vector<int> nums(n), ans(n);
    for(int i=0; i<n; i++) cin >> nums[i];
    for(int i=0; i<n; i++) {
        ans[i] = query(n+nums[i]-1, n+n-1, 0);
        update(n+nums[i]-1, 1);
    }
    for(int i=0; i<n; i++) cout << ans[i] << " \n"[i==(n-1)];
    return 0;
}