//wrong answer because it no work when they all negative you bobo
#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
 
int main() {
	ll min = LLONG_MAX; int minIdx = 0;
	ll max = LLONG_MIN; int maxIdx = 0;
	int n; cin >> n;
	ll sums[n+1]; sums[0] = 0;
	for(int i=1; i<n+1; i++) {
		int p; cin >> p;
		sums[i] = sums[i-1] + p;
		if(sums[i] > max) { 
			max = sums[i]; maxIdx = i;
			for(int j=i-1; j>=0; j--) {
				if(sums[j] < min) { min = sums[j]; minIdx = j; }
			}
		}
 
	}
	cout << sums[maxIdx]-sums[minIdx] << endl;
}
