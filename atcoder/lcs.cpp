#include <bits/stdc++.h>
using namespace std;

typedef vector<string> vs;
typedef vector<vs> vvs;
#define sz(x) (int)(x.size())

string mx(string& a, string& b) {
    if(sz(a) >= sz(b)) return a;
    else return b;
}

int main() {
    string s, t; cin >> s >> t;
    vvs DP(2, vs(sz(t)+1, ""));
    for(int k=1; k<=sz(s); k++) {
        for(int j=1; j<=sz(t); j++) {
            int i = k & 1;
            DP[i][j] = mx(DP[i^1][j], DP[i][j-1]);
            if(s[k-1] == t[j-1]) {
                string nw = DP[i^1][j-1]+s[k-1];
                DP[i][j] = mx(DP[i][j], nw);
            }
        }
    }
    cout << mx(DP[0][sz(t)], DP[1][sz(t)]) << endl;
    return 0;
}
