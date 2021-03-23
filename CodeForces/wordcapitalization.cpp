#include <iostream>
using namespace std;

int main() {
    string in; cin >> in;
    char last = ' ';
    for(string::iterator i=in.begin(); i<in.end(); i++) {
        if(isspace(last)) *i = toupper(*i);
        last = *i;
    }
    cout << in;
    return 0;
}
