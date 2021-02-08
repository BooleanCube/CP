//NOT WORKING!

#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int l[n];
    for(int i=0; i<n; i++) cin >> l[i];
    int count = 0;
    bool cube = true;
    for(int i=0; i<n-1; i++) {
        if(l[i] >= l[i+1]) {
            if(l[i] == 0 || l[i+1] == 0) {
                cout << "1";
                cube = false;
                break;
            }
            count += l[i] - (l[i+1]-1);
        }
    }
    if(cube) cout << count;
    return 0;
}
