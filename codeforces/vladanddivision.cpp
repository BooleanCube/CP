#include <bits/stdc++.h>
using namespace std;

int main() {
    int tc; cin >> tc;
    while(tc--) {
        int n; cin >> n;
        vector<int> nums(n);
        map<int, int> fq;
        for(int i=0; i<n; i++) {
            cin >> nums[i];
            fq[nums[i]]++;
        }
        long long b = (long long)(1 << 31)-1;
        int cnt = 0;
        for(int i : nums) {
            if(fq[i] <= 0) continue;
            fq[i]--;
            if(fq[i ^ b]) {
                fq[i ^ b]--;
                cnt++;
            }
        }
        cout << n-cnt << endl;
    }
    return 0;
}