#include <bits/stdc++.h>
using namespace std;

int main() {
    int t; cin >> t;
    for(int i=0; i<t; i++) {
        int n = 0; cin >> n;
        int odd = 0; int even = 0;
        for(int j=0; j<2*n; j++) {
            int a; cin >> a;
            if(a%2==0) ++even;
            else ++odd;
        }
        if(even == odd) cout << "Yes" << endl;
        else cout << "No" << endl;
    }
}
