#include <bits/stdc++.h>
using namespace std;

#define endl "\n"

int main() {
    // ios_base::sync_with_stdio(false);
    // cin.tie(NULL); cout.tie(NULL);
    int n, m, q; cin >> n >> m >> q;
    vector<int> w(n), fq(1<<n), wu(1<<n);
    vector<vector<int>> cache(1<<n, vector<int>(101, 0));
    int sow = 0;
    for(int &i : w) {
        cin >> i;
        sow += i;
    }
    for(int i=0; i<(1<<n); i++) {
        int v = 0;
        for(int j=0; j<n; j++) v += (i & (1<<j)) > 0 ? w[n-j-1] : 0;
        wu[i] = v;
    }
    for(int i=0; i<m; i++) {
        string t; cin >> t;
        int T = stoi(t, NULL, 2);
        fq[T]++;
    }
    for(int i=0; i<(1<<n); i++) {
		for(int j=0; j<(1<<n); j++) {
			if (sow-wu[i^j] > 100) continue;
			cache[i][sow-wu[i^j]] += fq[j];
		}
		for(int j=1; j<101; j++) cache[i][j] += cache[i][j-1];
	}
    for(int i=0; i<q; i++) {
        string t; int k; cin >> t >> k;
        int T = stoi(t, NULL, 2);
        cout << cache[T][k] << endl;
    }
    return 0;
}