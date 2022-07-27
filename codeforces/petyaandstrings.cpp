#include <bits/stdc++.h>
using namespace std;

int main() {
    string a,b; cin >> a >> b;
    transform(a.begin(), a.end(), a.begin(), ::tolower);
    transform(b.begin(), b.end(), b.begin(), ::tolower);
    vector<string> words;
    words.push_back(a); words.push_back(b);
    sort(words.begin(), words.end());
    if(a==b) cout << 0;
    else if(words.front() == a && words.back() == b) cout << -1;
    else cout << 1;
    return 0;
}
