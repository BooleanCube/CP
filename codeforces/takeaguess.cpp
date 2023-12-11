#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k; cin >> n >> k;
    vector<int> nums(n);
    cout << "and 1 2\nor 1 2\nand 2 3\nor 2 3\nand 1 3\nor 1 3" << endl;
    int x = 0, y = 0, z = 0;
    int t;
    cin >> t; x += t; cin >> t; x += t;
    cin >> t; y += t; cin >> t; y += t;
    cin >> t; z += t; cin >> t; z += t;
    nums[0] = (z+x-y)>>1;
    nums[1] = (x+y-z)>>1;
    nums[2] = (y+z-x)>>1;
    for(int i=3; i<n; i++) {
        cout << "and 1 " + to_string(i+1) << endl;
        cout << "or 1 " + to_string(i+1) << endl;
        int a, b; cin >> a >> b;
        nums[i] = a+b-nums[0];
    }
    sort(nums.begin(), nums.end());
    cout << "finish " << nums[k-1] << endl;
    return 0;
}
