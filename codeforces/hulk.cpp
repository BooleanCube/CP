#include <iostream>
using namespace std;

int main() {
    int n; cin >> n;
    if(n==1) cout << "I hate it";
    else {
        string o;
        for(int i=0; i<n; i++) {
            if(i%2==0) o += "I hate";
            else o += "I love";
            if(i==n-1) o += " it";
            else o += " that ";
        }
        cout << o;
    }
    return 0;
}
