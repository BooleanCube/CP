#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k; cin >> n >> k;
    vector<int>* days = new vector<int>;
    for(int i=0; i<n; i++) {
        int d; cin >> d;
        days->push_back(d);
    }
    int count = 0;
    for(int i=0; i<n; i++) {
        int d = days->at(i);
        if(d == 0) count++;
        if(d == -1) {
            int p = days->at(i-1);
            int x = p+1;
            if(p == k-1) x = 0;
            if(x == 0) count++;
            days->at(i) = x;
        }
    }
    cout << count << endl;
}
