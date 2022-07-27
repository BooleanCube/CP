//Wrong Answer
//Not Accepted

#include <iostream>
using namespace std;

int main() {
    int n; cin >> n;
    long m=0;
    bool flag = true;
    for(int i=0; i<n; i++) {
        int bill; cin >> bill;
        int changeNeeded = bill-25;
        if(m<changeNeeded) { flag = false; break; }
        else m-=changeNeeded;
        m+=bill;
    }
    if(flag) cout << "YES";
    else cout << "NO";
    return 0;
}
