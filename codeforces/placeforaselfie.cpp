#include <bits/stdc++.h>
#include <cmath>
#include <tuple>
using namespace std;

int main() {
    int t; cin >> t;
    for(int l=0; l<t; l++) {
        int n,m; cin >> n >> m;
        multiset<int> lines;
        for(int i=0; i<n; i++) {
            int k; cin >> k;
            lines.insert(k);
        }
        for(int i=0; i<m; i++) {
            long long a,b,c; cin >> a >> b >> c;
            long double num = b - sqrt(a)*sqrt(c)*2;
            long double num2 = b + sqrt(a)*sqrt(c)*2;
            auto it = lines.upper_bound(floor(num));
            if(it == lines.end()) cout << "NO\n";
            else {
                int k = *(it);
                if(k < num2) cout << "YES\n" << k << "\n";
                else cout << "NO\n";
            }
        }
        if(l < t-1) cout << "\n";
    }
    return 0;
}
