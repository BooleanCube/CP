#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    int oddCount = 0; int evenCount = 0;
    int lastEven = -1; int lastOdd = -1;
    int idx = -1;
    for(int i=0; i<n; i++) {
        int a; cin >> a;
        if(a%2==0) { evenCount++; lastEven = i+1; }
        else { oddCount++; lastOdd = i+1; }
        if(evenCount > 1 && lastOdd > -1) {
            idx = lastOdd;
            break;
        } else if(oddCount > 1 && lastEven > -1) {
            idx = lastEven;
            break;
        }
    }
    if(idx > -1) cout << idx;
    else if(evenCount > 1) cout << lastOdd;
    else cout << lastEven;
    return 0;
}
