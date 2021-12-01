#include <bits/stdc++.h>
using namespace std;

int findIndex(string a) {
    int idx;
    for(int i=0; i<a.length(); i++) {
        char c = a.at(i);
        if(c == 'L') idx = idx*2;
        else if(c == 'R') idx = idx*2+1;
        else if(idx != 1) idx = (int) floor(idx/2.0);
    }
    return idx;
}

vector<string> getPermutations(string t) {
    
}

int main() {
    int n; cin >> n;
    while(n-- > 0) {
        string s; cin >> s;
        string t; cin >> t;
        int current = findIndex(s);
        unordered_set<int> visitedIndexes = new unordered_set<>();
        vector<string> p = getPermutations(t);
        for(string a : p) unordered_set.insert(findIndex(a));
        cout << sizeof(visitedIndexes)/sizeof(visitedIndexes[0]) << endl;
    }
}
