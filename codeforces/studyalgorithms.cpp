#include <functional>
#include <iostream>
#include <iterator>
#include <queue>
#include <vector>
using namespace std;

int main (int argc, char *argv[]) {
    int n,x; cin >> n >> x;
    priority_queue<int, vector<int>, greater<int>> nums;
    for(int i=0; i<n; i++) { int a; cin >> a; nums.push(a); }
    int c = 0, s = 0;
    for(int i=0; i<n; i++) {
        s += nums.top();
        if(s > x) break;
        c++;
        nums.pop();
    }
    cout << c << endl;
    return 0;
}
