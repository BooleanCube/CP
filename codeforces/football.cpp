#include <iostream>
#include <string>
using namespace std;

int main() {
    string field; cin >> field;
    char last='a'; int con=0;
    bool dangerous = false;
    for(int i=0; i<field.length(); i++) {
        if(field.at(i)==last) ++con;
        else con = 1;
        if(con >= 7) {
            dangerous = true;
            break;
        }
        last = field.at(i);
    }
    if(dangerous) cout << "YES";
    else cout << "NO";
    return 0;
}
