#include <bits/stdc++.h>
using namespace std;

int main() {
    int t; cin >> t;
    for(int i=0; i<t; i++) {
        int n; cin >> n;
        set<int> a;
        for (int j=0; j<n; j++) {
            int aj; cin >> aj;
            aj %= 10;
            a.insert(aj);
        }
        vector<int> b(a.begin(), a.end());
        bool no = true;
        for(int j=0; j<n; j++) {
            for(int k=j+1; k<n; k++) {
                for(int l=k+1; l<n; l++) {
                    if((b[j]+b[k]+b[l])%10 == 3) {
                        cout << "YES" << endl;
                        no = false;
                        goto outer;
                    }
                }
            }
        }
outer:
        if(no) cout << "NO" << endl;
    }
    return 0;
}
