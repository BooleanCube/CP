#include <bits/stdc++.h>
using namespace std;

bool inBounds(int x, int y, int n) {
    return x>0 && y>0 && x<n && y<n;
}

int main() {
    int n; cin >> n;
    char map[n][n];
    int count[n][n];
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            cin >> map[i][j];
            count[i][j] = 0;
        }
    }
    count[0][0] = 1;
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            if(inBounds(i-1,j,n)) count[i][j] += count[i-1][j];
            if(inBounds(i,j-1,n)) count[i][j] += count[i][j-1];
        }
    }
    for(int i=0; i<n; i++) {
        for(int j : count[i]) {
            cout << j << " ";
        }
        cout <<endl;
    }
    cout << count[n-1][n-1] << endl;
    return 0;
}
