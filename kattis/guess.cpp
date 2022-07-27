#include <iostream>
using namespace std;

int main() {
    int min = 1, max = 1000;
    while(true) {
        int avg = (min+max)/2;
        cout << avg << endl;
        string pos; cin >> pos;
        if(pos == "higher") min = avg+1;
        else if(pos=="lower") max = avg-1;
        else break;
    }
    return 0;
}
