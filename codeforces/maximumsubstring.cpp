#include <bits/stdc++.h>
using namespace std;

vector<int> lcs(string s) {
    int ans = 1, temp = 1;
    int x = 0, y = 0;
    if(s[0]=='0')x++;
    else y++;
    for (int i = 1; i < s.size(); i++) {
        if(s[i] == '0') x++;
        else y++;
        if (s[i] == s[i - 1]) {
            ++temp;
        }
        else {
            ans = max(ans, temp);
            temp = 1;
        }
    }
    ans = max(ans, temp);
    vector<int> result(3);
    result[0]= ans;
    result[1] = x; result[2] = y;
    return result;
}

int main() {
    int t; cin >> t;
    for(int z=0; z<t; z++) {
        int n; cin >> n;
        string s; cin >> s;
        vector<int> r = lcs(s);
        cout << max((long long)(pow(r[0], 2)), ((long long)r[1]*(long long)r[2])) << '\n';
    }
    return 0;
}
