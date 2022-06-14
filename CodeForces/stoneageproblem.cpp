#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main (int argc, char *argv[]) {
    int n,q; cin >> n >> q;
    vector<ll> nums(n, 0);
    ll sum = 0;
    for(int i=0; i<n; i++) cin >> nums[i], sum += nums[i];
    for(int i=0; i<q; i++) {
        int t; cin >> t;
        if(t == 1) {
            int idx,rep; cin >> idx >> rep;
            sum += rep-nums[idx-1];
            nums[idx-1] = rep;
            cout << sum << endl;
        }
        else if(t == 2) {
            int add; cin >> add;
            sum = add*n;
            fill(nums.begin(), nums.end(), add);
            cout << sum << endl;
        }
    }
    return 0;
}
