#include <bits/stdc++.h>
using namespace std;

void solve() {
    int lo = 1, hi; cin >> hi;
    while (lo < hi) {
        int mid = (lo + hi) >> 1;
        vector<int> l;
        for (int i = lo; i <= mid; ++i) l.push_back(i);
        cout << "? " << l.size();
        for (int i : l) cout << " " << i;
        cout << endl;

        string a; cin >> a;

        cout << "? " << l.size();
        for (int i : l) cout << " " << i;
        cout << endl;

        string b; cin >> b;

        if (a == "YES" || b == "YES") hi = mid;
        else lo = mid + 1;
    }
    cout << "! " << lo << endl;
    string a; cin >> a;
}

int main() {
    solve();
    return 0;
}

