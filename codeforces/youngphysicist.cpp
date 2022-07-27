#include <iostream>
using namespace std;

int main() {
    int n; cin >> n;
    int x=0, y=0, z=0;
    for(int i=0; i<n; i++) {
        int xt,yt,zt; cin >> xt >> yt >> zt;
        x+=xt; y+=yt; z+=zt;
    }
    if(x==0 && y==0 && z==0) cout << "YES";
    else cout << "NO";
    return 0;
}
