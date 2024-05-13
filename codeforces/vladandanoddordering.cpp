#include <bits/stdc++.h>
using namespace std;

#define int long long
#define ld long double

const ld EPS = 1e-6;

signed main() {
    int tc; cin >> tc;
    while(tc--) {
        int n, k, num = 1; cin >> n >> k;
        int sum = 0;
        for(int i=1; i<30; i++) {
            int val = (n) / (1 << i);
            // cout << "val " << val << endl;
            sum += val;
            // cout << "sum " << sum << endl;
            num = i;
            if(sum >= k) {
                sum -= val;
                break;
            }
            // if(ceil(((ld)(n))/(1 << i)) == 1) break;
        }
        cout << k << " " << sum << " " << num << endl;
        int s = (1 << (num-1)), d = (1 << num);
        cout << s << " " << d << " " << (k - round(sum) - 1) << endl;
        cout << (int)(k - round(sum) - 1) * d + s << endl;
    }
    return 0;
}