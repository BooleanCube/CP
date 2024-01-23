#include <bits/stdc++.h>
using namespace std;

bool cmp(string a, string b) {
    return (a+b < b+a);
}

int main() {
    int n; cin >> n;
    vector<string> s(n);
    for(int i=0; i<n; i++) cin >> s[i];
    sort(s.begin(), s.end(), cmp);
    for(int i=0; i<n; i++) cout << s[i];
    cout << endl;
    return 0;
}
