#include <bits/stdc++.h>
using namespace std;

void find(vector<int>& parent, vector<int>& size, int n, int si) {
    int p = parent[n];
    if(p == n) return;
    size[p]+=si;
    find(parent, size, p, si);
}

int main() {
    int n; cin >> n;
    vector<int> parent(n+1);
    vector<int> size(n+1, 0);
    for(int i=1; i<=n; i++) parent[i] = i;
    for(int i=2; i<=n; i++) {
        int e; cin >> e;
        parent[i] = e;
        find(parent, size, i, size[i]+1);
    }
    string s;
    for(int i=1; i<=n; i++)
        s += to_string(size[i]) + " ";
    s.erase(s.find_last_not_of(" \n\r\t")+1);
    cout << s << endl;
    return 0;
}
