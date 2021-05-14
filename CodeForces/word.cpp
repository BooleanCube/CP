#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <cctype>
using namespace std;

int main() {
    int upc = 0;
    string s; cin >> s;
    for(char c : s) { if(isupper(c)) ++upc; }
    if(upc>s.length()-upc) std::transform(s.begin(), s.end(), s.begin(), [](unsigned char c){ return std::toupper(c); });
    else std::transform(s.begin(), s.end(), s.begin(), [](unsigned char c){ return std::tolower(c); });
    cout << s;
    return 0;
}
