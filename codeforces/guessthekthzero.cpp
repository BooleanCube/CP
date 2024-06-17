#include <bits/stdc++.h>
using namespace std;

int n, t;

int search(int k) {
    int lo = 0, hi = n-1;
    while(lo < hi) {
        int mid = (lo + hi) / 2;
        cout << "? " << 1 << " " << mid+1 << endl;
        int sm; cin >> sm;
        if(mid + 1 - sm < k) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

int main() {
    cin >> n >> t;
    while(t--) {
        int k; cin >> k;
        int ans = search(k) + 1;
        cout << "! " << ans << endl;
    }
    return 0;
}