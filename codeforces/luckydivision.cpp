#include <iostream>
using namespace std;

int main() {
    int n; cin >> n;
    bool cube = false;
    int luckies[12] = {4,7,47,74,44,444,474,447,774,744,777,477};
    for(int i=0; i<12; i++) if(n%luckies[i]==0) cube=true;
    if(cube) cout << "YES";
    else cout << "NO";
    return 0;
}
