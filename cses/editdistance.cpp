#include <bits/stdc++.h>
using namespace std;

vector<vector<array<int, 2>>> DP;

int lcs(string& a, string& b, int n, int m) {
    DP = vector<vector<array<int, 2>>>(n+1, vector<array<int, 2>>(m+1));
    for(int i = 0; i<=n; i++) {
        for(int j = 0; j<=m; j++) {
            if(i == 0 || j == 0) DP[i][j][0] = 0;
            else if(a[i - 1] == b[j - 1]) {
                DP[i][j][0] = DP[i-1][j-1][0] + 1;
                DP[i][j][1] = 1;
            }
            else DP[i][j][0] = max(DP[i-1][j][0], DP[i][j-1][0]);
        }
    }
    return DP[n][m][0];
}

int main() {
    string a, b; cin >> a >> b;
    int n = a.size(), m = b.size();
    int l = lcs(a, b, n, m);
    cout << l << endl;
    int idx1 = 0, idx2 = 0;
    for(int i=n; i>=0; i--) {
        for(int j=m; j>=0; j--) {
            if(DP[i][j][1] && DP[i][j][0] == l) {
                idx1 = i;
                idx2 = j;
                goto outer;
            }
        }
    }
outer:
    cout << idx1 << " " << idx2 << endl;
    cout << max(idx1-l, idx2-l) + max(n-idx1, m-idx2) << endl;
    return 0;
}