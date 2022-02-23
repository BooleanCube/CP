#include <bits/stdc++.h>
using namespace std;

int indexOf(int a[], int n, int startIdx) {

}
 
int main() {
	int n, s; cin >> n >> s;
	int a[n], o[n];
	for(int i=0; i<n; i++) { cin >> a[i]; o[i] = a[i]; }
	sort(a, a+n);
	int l = 0, r = n-1;
	bool met = 0;
	while(l<r) {
		if(a[l] + a[r] <= s) l++;
		else {
			int 
			for(int i=l+1; i<r; i++) {

			}
			r--;
			int idxR = distance(o,find(o, o+n, a[r]))+1;
			int idxL = distance(o,find(o, o+n, a[l]));
			cout << to_string(idxR) << " " << to_string(n-idxL) << endl;
			met = 1;
			break;
		}
	}
	if(!met) cout << "IMPOSSIBLE" << endl;
}
