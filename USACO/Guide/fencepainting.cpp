//Rectangle Geometry

#include <bits/stdc++.h>
using namespace std;
int main() {
    freopen("paint.in", "r", stdin);
    freopen("paint.out", "w", stdout);
    int a, b, c, d; cin >> a >> b >> c >> d;
    int total = (b-a)+(d-c);
    int intersection = max(min(b, d) - max(a, c), 0);
    cout << total - intersection;
}
