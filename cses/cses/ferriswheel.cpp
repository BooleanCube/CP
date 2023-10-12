#include <bits/stdc++.h>
#include <iterator>
#include <set>
using namespace std;

int main(int argc, char *argv[]) {
    int n, x; cin >> n >> x;
    vector<int> p(n);
    for(int i=0; i<n; i++) cin >> p[i];
    sort(begin(p), end(p));
    int doubles = 0, l = 0, r = n-1;
    while(r>l) {
        int sum = p[l]+p[r];
        //cout << p[0] << " " << p[i] << " " << sum << endl;
        if(sum <= x) {
            doubles++;
            l++;
        }
        r--;
    }
    int singles = n-2*doubles;
    cout << singles + doubles << endl;
    return 0;
}
