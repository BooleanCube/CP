//incomplete
#include <bits/stdc++.h>
using namespace std;

int lengthSubstring(vector<bool>& bits, int n) {
	int m = -1;
	int c = 1;
	for(int i=1; i<n; i++) {
		if(bits[i-1]==bits[i]) c++;
		else {
			m = max(m, c);
			c = 1;
		}
	}
	m = max(m,c);
	return m;
}

int main() {
	vector<bool> bits;
	string inp; cin >> inp;
	for(auto a : inp) bits.push_back(a=='1');
	int n; cin >> n;
	for(int i=0; i<n; i++) {
		int idx; cin >> idx;
		cout << idx << endl;
		bits[idx] = !bits[idx];
		for(int i=0; i<inp.length(); i++) cout << bits[idx] << " ";
		cout << endl;
		cout << lengthSubstring(bits, inp.length()) << " ";
	}
}
