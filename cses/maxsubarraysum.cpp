#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
 
int main() {
	int n; cin >> n;
	ll sums[n+1]; sums[0] = 0;
	for(int i=1; i<n+1; i++) {
		int p; cin >> p;
		sums[i] = sums[i-1] + p;
	}
	ll maxSum = sums[1];
	ll minPfx = sums[0];
	for(int i=1; i<=n; i++) {
		maxSum = max(maxSum, sums[i]-minPfx);
		minPfx = min(minPfx, sums[i]);
	}
	cout << maxSum << endl;
}
