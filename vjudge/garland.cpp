#include <bits/stdc++.h>
using namespace std;

int main(int argc, char *argv[]) {
    int n; cin >> n;
    vector<int> bulbs(n+1);
    int odds = 0, evens = 0;
    for(int i=1; i<=n; i++) {
        cin >> bulbs[i];
        if(bulbs[i]==0) continue;
        if(bulbs[i]%2) odds++;
        else evens++;
    }
    odds = ceil(n/2)-odds; evens = floor(n/2)-evens;
    bool fl = 0, ll = 0;
    int complexity = 0;
    for(int i=1; i<n; i++) {
        int c = bulbs[i];
        if(c==0) {
            if(i-1==0) fl = 1;
            else if(i+1>n) ll = 1;
            else {
                int fe = bulbs[i-1]%2, se = bulbs[i+1]%2;
                if(fe==se) {
                    if(fe && odds > 0) odds--;
                    else if(fe==0 && evens>0) evens--;
                    else if(fe) { evens--; complexity+=2; }
                } else complexity++;
            }
        }
    }
    if(fl) {
        if(bulbs[2] && odds > 0) odds--;
        else if(bulbs[2]==0 && evens>0) evens--;
        else complexity++;
    }
    if(ll) {
        if(bulbs[n-2] && odds > 0) odds--;
        else if(bulbs[n-2]==0 && evens>0) evens--;
        else complexity++;
    }
    cout << complexity << endl;
    return 0;
}
