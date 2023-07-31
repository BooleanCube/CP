#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k; cin >> n >> k;
    vector<int> l(n);
    for(int i=0; i<n; i++) cin >> l[i];
    map<int, int> servers;
    servers[l[0]] = 1;
    int last = l[0];
    for(int i=1; i<n; i++) {
        int request = l[i];
        auto it = servers.upper_bound(request - 1000);
        if(it != servers.begin()) {
            it--;
            int s = (*it).first, e = (*it).second;
            if(request - s >= 1000) {
                servers.erase(it);
                servers[request] = 1;
                last = request;
                continue;
            }
        }
        int s = last, e = servers[last];
        if(request - s < 1000 && e < k) servers[s]++;
        else if(request - s < 1000) {
            servers[request] = 1;
            last = request;
        }
    }
    cout << servers.size() << "\n";
    return 0;
}
