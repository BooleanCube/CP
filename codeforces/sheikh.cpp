#include <bits/stdc++.h>
using namespace std;

#define sp <<" "<<
#define int long long

void solve() {
    int n, q; cin >> n >> q;
    vector<int> nums(n);
    for(int &i : nums) cin >> i;
    vector<int> psum(n+1), pxor(n+1);
    for(int i=1; i<=n; i++) {
        psum[i] = psum[i-1] + nums[i-1];
        pxor[i] = pxor[i-1] ^ nums[i-1];
    }
    while(q--) {
        int L, R; cin >> L >> R;
        int lIdx = 0, rIdx = 0, ans = -1;
        for(int i=L; i<=R; i++) {
            int lo = i, hi = R, t = (psum[R]-psum[i-1]) - (pxor[R]^pxor[i-1]);
            while(lo < hi) {
                int mid = lo + ((hi- lo) >> 1);
                int val = (psum[mid] - psum[i-1]) - (pxor[mid] ^ pxor[i-1]);
                if(val < t) lo = mid+1;
                else hi = mid;
            }
            if(t > ans) {
                ans = t;
                lIdx = i; rIdx = lo;
            } else if(t == ans && (lo-i) < (rIdx-lIdx)) {
                ans = t;
                lIdx = i; rIdx = lo;
            }
        }
        cout << lIdx << " " << rIdx << endl;
    }
}

signed main() {
    int tc; cin >> tc;
    while(tc--) solve();
    return 0;
}
