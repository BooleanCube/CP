#include <bits/stdc++.h>
using namespace std;

int main() {
    int count = 0;
    vector<int> guesses = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 4, 9, 25, 49};
    for(int i : guesses) {
        cout << "? " << i << endl;
        string r; cin >> r;
        if(r == "yes") count++;
    }
    if(count <= 1) cout << "! prime" << endl;
    else cout << "! composite" << endl;
}
