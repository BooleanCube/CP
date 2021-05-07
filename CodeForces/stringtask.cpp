#include <iostream>
using namespace std;

int main() {
    string sin, sout; cin >> sin;
    int len=sin.length();
    for(int i=0; i<len; i++) {
        if(sin[i]=='a'||sin[i]=='e'||sin[i]=='i'||sin[i]=='o'||sin[i]=='u'||sin[i]=='y'||sin[i]=='A'||sin[i]=='E'||sin[i]=='O'||sin[i]=='I'||sin[i]=='U'||sin[i]=='Y') continue;
        else { sout+='.'; sout+=towlower(sin[i]); }
    }
    cout << sout;
    return 0;
}
