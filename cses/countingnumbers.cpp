#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<pii> vp;
typedef vector<vp> vvp;
#define f first
#define s second
#define sz(x) (int)(x.size())

string cfill(string s, int n, char c) {
    while(sz(s) < n) s = c + s;
    return s;
}

vvi memo(18, vi(10, -1));
string curs = cfill("", 18, '0'), curb = cfill("", 18, '9'), a, b;

int DP(int idx, int pd, int flag) {
    cout << idx << " " << pd << " " << curs << " " << curb << endl;
    if(curs > b || curb < a) return 0;
    if(idx == 18) return 1;
    if(pd > -1 && memo[idx][pd] != -1) return memo[idx][pd];
    if(flag) flag = !(a[idx] > '0' || b[idx] > '0');
    int ans = 0;
    for(int i=0; i<=9; i++) {
        if(i == pd) continue;
        curs[idx] = i+'0'; curb[idx] = i+'0';
        ans += DP(idx+1, (flag ? -1 : i), flag);
        curs[idx] = '0'; curb[idx] = '9';
    }
    return memo[idx][pd] = ans;
}

int main() {
    cin >> a >> b; a = cfill(a, 18, '0'); b = cfill(b, 18, '0');
    cout << a << " " << b << endl;
    cout << DP(0, -1, 1) << endl;
    return 0;
}
