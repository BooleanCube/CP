#include <bits/stdc++.h>
using namespace std;

int main() {
    int t; cin >> t;
    while(t-- > 0) {
        string s; cin >> s;
        int n = s.size();
        int k = 57;
        int count[10] = {0,0,0,0,0,0,0,0,0,0};
        for(int i=n-1; i>=0; i--) {
            char c = s[i];
            int d = c-'0';
            if(c <= char(k)) {
                count[d]++;
                k=c;
            }
            else count[min(d+1,9)]++;
        }
        for(int i=0; i<=9; i++)
            while(count[i]-- > 0) cout << i;
        cout << '\n';
    }
}
