#include <bits/stdc++.h>
using namespace std;

#define int long long

signed main() {
    int n, k; cin >> n >> k;
    vector<int> nums(n);
    for(int i=0; i<n; i++) cin >> nums[i];
    set<pair<int,int>> pq;
    for(int i=0; i<n; i++) pq.insert(make_pair(nums[i], i));
    vector<bool> vis(n);
    while(!pq.empty()) {
        pair<int, int> cur = *(--pq.end()); pq.erase(--pq.end());
        int val = cur.first, idx = cur.second;
        vis[idx] = 1;
        if(idx && !vis[idx-1]) {
            pq.erase(pq.find(make_pair(nums[idx-1], idx-1)));
            nums[idx-1] = min(max(nums[idx-1], val-k), val+k);
            pq.insert(make_pair(nums[idx-1], idx-1));
        }
        if(idx<n-1 && !vis[idx+1]) {
            pq.erase(pq.find(make_pair(nums[idx+1], idx+1)));
            nums[idx+1] = min(max(nums[idx+1], val-k), val+k);
            pq.insert(make_pair(nums[idx+1], idx+1));
        }
    }
    for(int i=0; i<n; i++) cout << nums[i] << " \n"[i==n-1];
    return 0;
}