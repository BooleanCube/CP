#include <bits/stdc++.h>
#include <queue>
using namespace std;

int main() {
    int n; cin >> n;
    queue<string>* colors = new queue<string>; 
    for(int i=0; i<n; i++) { 
        int t; cin >> t;
        if(t == 1) {
            string c; cin >> c;
            colors->push(c);
        } else {
            string c = colors->front();
            colors->pop();
            colors->push(c);
            cout << c << '\n';
        }
    }
}
