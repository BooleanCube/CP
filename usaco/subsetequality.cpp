#include <bits/stdc++.h>
#include <unordered_map>
#include <unordered_set>
using namespace std;

int main() {
    string s; cin >> s;
    string t; cin >> t;

    unordered_map<char, set<int>> idxMap;
    for(int i=0; i<t.size(); i++) {
        char l = t[i];
        idxMap[l].insert(i);
    }

    unordered_set<char> invalid;
    vector<int> edges(s.size());
    
    for(int i=0; i<s.size(); i++) {
        char l = s[i];
        if(invalid.count(l)) continue;
        if(idxMap.count(l) == 0 || idxMap[l].size() == 0) {
            invalid.insert(l);
            continue;
        }
        int idx = *idxMap[l].begin();
        idxMap[l].erase(idx);
        edges[i] = idx;
    }

    return 0;
}
