#include <bits/stdc++.h>
using namespace std;

int main() {
    string s; cin >> s;
    sort(s.begin(), s.end());
    char last; int counter=0;
    for(int i=0; i<s.length(); i++) {
        if(s.at(i)!=last) ++counter;
        last=s.at(i);
    }
    if(counter%2==0) cout << "CHAT WITH HER!";
    else cout << "IGNORE HIM!";
    return 0;
}
