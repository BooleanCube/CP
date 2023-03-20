#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    string out = "";
    while (t--) {
        int n, q;
        cin >> n >> q;
        vector<int> l(n);
        for (int i = 0; i < n; i++) {
            cin >> l[i];
        }
        vector<int> psum(n + 1);
        for (int i = 1; i <= n; i++) {
            psum[i] = l[i-1] + psum[i-1];
        }
        int ts = psum[n]-psum[0];
        while (q--) {
            int s, e, k;
            cin >> s >> e >> k;
            int r = e - s + 1;
            if ((ts - psum[e] - psum[s-1]) & 1) {
                out += ((k*r) & 1) ? "no\n" : "yes\n";
            } else {
                out += ((k*r) & 1) ? "yes\n" : "no\n";
            }
        }
    }
    cout << out;
    return 0;
}
