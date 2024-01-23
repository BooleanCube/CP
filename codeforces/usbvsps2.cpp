#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    int m;
    cin >> m;

    priority_queue<int, vector<int>, greater<int>> u, p, t;

    for (int i = 0; i < m; ++i) {
        int cost;
        string port;
        cin >> cost >> port;

        if (port[0] == 'U') {
            u.push(cost);
        } else {
            p.push(cost);
        }
    }

    ll cnt = 0, price = 0;

    for (int i = 0; i < a; ++i) {
        if (u.empty()) break;
        cnt++;
        price += u.top();
        u.pop();
    }

    for (int i = 0; i < b; ++i) {
        if (p.empty()) break;
        cnt++;
        price += p.top();
        p.pop();
    }

    while(!u.empty()) { t.push(u.top()); u.pop(); }
    while(!p.empty()) { t.push(p.top()); p.pop(); }

    for (int i = 0; i < c; ++i) {
        if (t.empty()) break;
        cnt++;
        price += t.top();
        t.pop();
    }

    cout << cnt << " " << price << endl;

    return 0;
}
