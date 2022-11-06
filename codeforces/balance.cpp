#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll kmex(set<ll>& s, ll k) {
	for(int i=1; i<s.size()+2; i++) {
		if(s.count(k*i) == 0) return k*i;
	}
	return 0;
}

int main() {
	int q; cin >> q;
	set<ll> *s = new set<ll>;
	while(q--) {
		string t; cin >> t;
		ll x; cin >> x;
		if(t == "+") s->insert(x);
		if(t == "?") cout << kmex(*s, x) << endl;
	}
	return 0;
}