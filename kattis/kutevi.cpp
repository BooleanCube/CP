#include <bits/stdc++.h>
using namespace std;

int mod(int a, int b) {
    int m = a%b;
    if(m < 0) m += b;
    return m;
}

int main() {
    int n, k; cin >> n >> k;
    vector<int> nums;
    for(int i=0; i<n; i++) {
        int a; cin >> a;
        for(int i=0; i<360; i++) nums.emplace_back(a);
        for(int i=0; i<360; i++) nums.emplace_back(-a);
    }
    sort(nums.begin(), nums.end());
    vector<int> DP(360);
    DP[0] = 1;
    for(int i=0; i<nums.size(); i++) DP[abs(nums[i])] = 1;
    for(int i=0; i<nums.size(); i++) {
        int val = nums[i];
        for(int j=360; j>=0; j--) {
            if(DP[mod(j-val, 360)]) DP[j] = 1;
        }
    }
    for(int t=0; t<k; t++) {
        int T; cin >> T;
        cout << (DP[T] ? "YES" : "NO") << endl;
    }
    return 0;
}