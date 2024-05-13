#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<map<int, int>> vm;
typedef vector<vm> vvm;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int tc; cin >> tc;
    while(tc--) {
        int n, m; cin >> n >> m;
        vvi grid(n, vi(m)), psp(n+1, vi(m+1)), psn(n+1, vi(m+1));
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                cin >> grid[i][j];
                psp[i+1][j+1] += psp[i+1][j] + psp[i][j+1] - psp[i][j];
                psn[i+1][j+1] += psn[i+1][j] + psn[i][j+1] - psn[i][j];
                if(grid[i][j] == 1) psp[i+1][j+1]++;
                else psn[i+1][j+1]++;
            }
        }
        int p = n + m - 1;
        if (p & 1) {
            cout << "NO" << endl;
            continue;
        }
    }
    return 0;
}