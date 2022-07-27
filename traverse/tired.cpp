#include <algorithm>
#include <bits/stdc++.h>
#include <iterator>
using namespace std;

int main (int argc, char *argv[]) {
    int t; cin >> t;
    while(t-- > 0) {
        int n; cin >> n;
        vector<int> nums(n);
        for(int i=0; i<n; i++) cin >> nums[i];
        set<int> check;
        bool a = true;
        copy(nums.begin(), nums.end(), inserter(check, check.end()));
        for(int i : check) {
            int o=0;
            for(int j=0; j<n; j++) {
                if(nums[j] == i) o++;
            }
            if(o>ceil(n/2)) a = false;
        }
        if(a) cout << "YES\n";
        else cout << "NO\n";
    }
    return 0;
}
