#include <bits/stdc++.h>
using namespace std;

int count(string s, char t) {
    int ans = 0;
    for(int i=0; i<s.size(); i++) if(s[i] == t) ans++;
    return ans;
}

int main() {
    int tc; cin >> tc;
    while(tc--) {
        int n; cin >> n;
        string s; cin >> s;
        if(n == count(s, '?')) {
            for(int i=0; i<n; i++) cout << "BR"[i&1];
            cout << endl;
            continue;
        }
        for(int i=1; i<n; i++) {
            if(s[i] == '?' && s[i-1] != '?') 
                s[i] = "BR"[s[i-1] == 'B'];
        }
        reverse(s.begin(), s.end());
        for(int i=1; i<n; i++) {
            if(s[i] == '?' && s[i-1] != '?') 
                s[i] = "BR"[s[i-1] == 'B'];
        }
        reverse(s.begin(), s.end());
        cout << s << endl;
    }
    return 0;
}