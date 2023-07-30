#include <bits/stdc++.h>
using namespace std;

#define int long long

signed main() {
    int n, m, l; cin >> n >> m >> l;
    vector<int> hairs(n);
    for(int i=0; i<n; i++) cin >> hairs[i];
    set<int> start, end;
    bool flag = 0;
    for(int i=0; i<n; i++) {
        if(!flag && hairs[i] > l) {
            start.insert(i);
            flag = 1;
        }
        if(flag && hairs[i] <= l) {
            end.insert(i-1);
            flag = 0;
        }
    }
    if(flag) end.insert(n-1);
    while(m--) {
        int op; cin >> op;
        if(op) {
            int a, b; cin >> a >> b; a--;
            hairs[a] += b;
            if(hairs[a] <= l+b && hairs[a] > l) {
                int s = start.count(a+1), e = end.count(a-1);
                if(s>0 && e>0) {
                    start.erase(a+1);
                    end.erase(a-1);
                } else if(s>0) {
                    start.erase(a+1);
                    start.insert(a);
                } else if(e>0) {
                    end.erase(a-1);
                    end.insert(a);
                } else {
                    start.insert(a);
                    end.insert(a);
                }
            }
        }
        else cout << start.size() << "\n";
    }
    return 0;
}
