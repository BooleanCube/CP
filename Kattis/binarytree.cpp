#include <bits/stdc++.h>
using namespace std;

int findIndex(string a, int idnx) {
    int idx = idnx;
    for(int i=0; i<a.length(); i++) {
        char c = a.at(i);
        if(c == 'L') idx = idx*2;
        else if(c == 'R') idx = idx*2+1;
        else if(idx != 1) idx = (int) floor(idx/2.0);
    }
    return idx;
}

unordered_set<string> getPermutations(string t) {
    unordered_set<string> *r = new unordered_set<string>();
	deque<string> *stack = new deque<string>();
	stack->push_back("");
	//while
	return *r;
}

int main() {
    int n; cin >> n;
    while(n-- > 0) {
        string s; cin >> s;
        string t; cin >> t;
        int current = findIndex(s, 1);
        unordered_set<int> *visitedIndexes = new unordered_set<int>();
        unordered_set<string> p = getPermutations(t);
        for(string a : p) visitedIndexes->insert(findIndex(a, current));
        cout << visitedIndexes->size() << endl;
    }
}
