#include <bits/stdc++.h>
using namespace std;

int findIndex(string a, int idnx) {
    int idx = idnx;
    for(long unsigned int i=0; i<a.length(); i++) {
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
    r->insert("");
    long unsigned int prevLength = 0;
    long unsigned int s = -1;
    for(long unsigned int i=0; i<stack->size(); i++) {
	string prefix = stack->front();
	stack->pop_front();
	if(prefix.length() > prevLength) s=0;
	else s++;
        for(long unsigned int j=s; j<t.length(); j++) {
	    string total = prefix + t.at(j);
	    stack->push_back(total);
	    r->insert(total);
	    prevLength = prefix.length() + 1;
	}
    }
    return *r;
}

int main() {
    int n; cin >> n;
	int o = n;
    while(n-- > 0) {
        string s; cin >> s;
        string t; cin >> t;
        int current = findIndex(s, 1);
        unordered_set<int> *visitedIndexes = new unordered_set<int>();
        unordered_set<string> p = getPermutations(t);
        for(string a : p) visitedIndexes->insert(findIndex(a, current));
        cout << "Case " << o-n << ": " << visitedIndexes->size() % 21092013 << endl;
    }
}
