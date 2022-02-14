//wrong answer because minIdx cant be greater than maxIdx you bobo
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
		if(sums[i] < min) { min = sums[i]; minIdx = i; }
		if(sums[i] > max) { max = sums[i]; maxIdx = i; }
	}
	cout << min << " " << max << " " << minIdx << " " << maxIdx << endl;
	cout << sums[maxIdx]-sums[minIdx] << endl;
}
