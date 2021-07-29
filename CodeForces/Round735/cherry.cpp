//accepted
#include <bits/stdc++.h>
using namespace std;

int main() {
    int t; cin >> t;
    for(int l=0; l<t; l++) {
        long long max = 0;
        int n; cin >> n;
        long long nums[n];
        for(int i=0; i<n; i++) cin >> nums[i];
        for(long long i=0; i<n; i++) {
            for(long long j=i+1; j<n; j++) {
                long long kmax = 0, kmin = 1000001;
                bool cube = false;
                for(int k=i; k<=j; k++) {
                    if(nums[k] > kmax) kmax = nums[k];
                    if(nums[k] < kmin) kmin = nums[k];
                    cube = true;
                }
                //cout << i << " " << j << " " << kmax << " " << kmin << endl;
                long long value;
                if(cube) value = kmin*kmax;
                else value = nums[i]*nums[j];
                //cout << value << endl;
                if(value > max) max = value;
            }
        }
        cout << max << endl;
    }
    return 0;
}
