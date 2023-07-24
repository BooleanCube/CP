#include <algorithm>
#include <bits/stdc++.h>
#include <utility>
using namespace std;

using ll = long long;

int findn(vector<int>& indices, map<int, ll>& intervals, int idx, ll mx) {
    auto it = lower_bound(indices.begin(), indices.end(), idx);
    if(it == indices.end()) {
        it--;
        int bsidx = *it;
        int diff = mx-intervals[bsidx]+1;
        int start = intervals[bsidx]+diff;
        int sidx = bsidx+1;
        return idx-sidx+start;
    }
    int bsidx = *it;
    int diff = bsidx-idx;
    return intervals[bsidx]-diff;
}

int main() {
    int t; cin >> t;
    while(t--) {
        int n,k; cin >> n >> k;
        vector<ll> nums;
        nums.push_back(0);
        for(int i=0; i<n; i++) {
            ll a; cin >> a;
            nums.push_back(a);
        }
        sort(nums.begin(), nums.end());
        map<int, ll> intervals;
        vector<int> indices;
        int last = 0;
        for(int i=1; i<=n; i++) {
            int diff = nums[i] - nums[i-1];
            if(diff > 1) {
                indices.push_back(last+diff-1);
                intervals[last+diff-1] = nums[i]-1;
                last += diff-1;
            }
        }
        ll mx = nums[nums.size()-1];
        ll cur = findn(indices, intervals, 1, mx);
        for(int i=0; i<k-1; i++) {
            cur = findn(indices, intervals, cur, mx);
        }
        cout << cur << endl;
    }
}
