#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> graph;
vector<int> strength;

int main() {
    int tc; cin >> tc;
    while(tc--) {
        int n, m; cin >> n >> m;
        graph = vector<vector<int>>(n);
        strength = vector<int>(n);
        for(int i=0; i<n; i++) cin >> strength[i];
    }
    return 0;
}