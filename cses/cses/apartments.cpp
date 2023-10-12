#include <bits/stdc++.h>
#include <iterator>
#include <valarray>
using namespace std;

#define ll long long
#define vi vector<int>
#define mi multiset<int>

int main() {
    int n,m,k; cin >> n >> m >> k;
    vi clients(n);
    mi apartments;
    for(int i=0; i<n; i++) cin >> clients[i];
    for(int i=0; i<m; i++) {
        int a; cin >> a;
        apartments.insert(a);
    }
    sort(begin(clients), end(clients));
    int cnt = 0;
    for(int i=0; i<n; i++) {
        if(apartments.size() == 0) break;
        int client = clients[i];
        auto it = apartments.lower_bound(client-k);
        if(abs(*it-client)<=k) { cnt++; apartments.erase(it); }
    }
    //int ans = cnt;
    cout << cnt << endl;
    return 0;
}
