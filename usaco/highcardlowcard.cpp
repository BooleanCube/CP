#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("cardgame.in", "r", stdin);
    freopen("cardgame.out", "w", stdout);
    int n; cin >> n;
    vector<int> elsie(n);
    multiset<int> cands;
    for(int i=1; i<=2*n; i++) cands.insert(i);
    for(int i=0; i<n; i++) {
        cin >> elsie[i];
        cands.erase(elsie[i]);
    }
    sort(elsie.begin(), elsie.begin()+n/2); reverse(elsie.begin(), elsie.begin()+n/2);
    sort(elsie.begin()+n/2, elsie.end());
    int fh = 0, sh = 0;
    for(int i=0; i<n/2; i++) {
        auto it = --cands.end();
        if(*it > elsie[i]) {
            fh++;
            cands.erase(it);
        }
    }
    for(int i=n/2; i<n; i++) {
        auto it = cands.lower_bound(elsie[i]);
        if(it != cands.begin()) {
            it--;
            sh++;
            cands.erase(it);
        }
    }
    cout << fh + sh << endl;
    return 0;
}