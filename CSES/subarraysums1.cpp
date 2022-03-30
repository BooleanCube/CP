#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
	ll n,x; cin >> n >> x;
	vector<ll> nums(n-1,0);
	for(int i=0; i<n; i++) cin >> nums[i];
	int l=0,r=0;
	ll sum=0, c=0;
	while(r<n) {
		sum += nums[r];
		cout << l << " " << r << " " << sum << endl;
		if(sum > x) sum -= nums[l], l++;
		if(sum == x) c++;
		r++;
	}
	cout << c << endl;
}
