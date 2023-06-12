#include <bits/stdc++.h>
#include <iterator>
using namespace std;

int main() {
    int t; cin >> t;
    while(t--) {
        int n; cin >> n;
        multiset<int> a;
        multiset<int> b;
        for(int i=0; i<n; i++) {
            int x; cin>> x;
            a.insert(x);
        }
        for(int i=0; i<n; i++) {
            int x; cin>> x;
            b.insert(x);
        }
        auto it = a.begin();
        long long taken = 0;
        long long ans = 1;
        bool poss = true;
        while(it != a.end()) {
            int val = *it;
            auto itr = b.upper_bound(val-1);
            if(itr == b.begin()) {
                poss = false;
                break;
            }
            itr--;
            long long idx = distance(b.begin(), itr);
            if(idx < taken) {
                poss = false;
                break;
            } else {
                ans *= idx+1-taken;
                ans %= 1000000007;
                taken++;
            }
            it++;
        }
        if(!poss) {
            cout << 0 << "\n";
        } else {
            cout << ans << "\n";
        }
    }
    return 0;
}
