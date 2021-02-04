#include <iostream>
using namespace std;

int main() {
    int a,b,c,d,p,m,g;
    cin>>a>>b>>c>>d>>p>>m>>g;
    int sum=0;
    int counter = 0;
    bool active = true;
    while(sum<p) {
        if(active) {
            sum+=a;
            active=false;
        } else {
            sum+=b;
            active = true;
        }
    }
    if(active) counter++;
    active = true;
    sum = 0;
    while(sum<p) {
        if(active) {
            sum+=c;
            active = false;
        } else {
            sum += d;
            active = true;
        }
    }
    if(active) counter++;
    active = true;
    sum = 0;
    if(counter == 2) cout << "none\n";
    if(counter == 1) cout << "one\n";
    if(counter == 0) cout << "both\n";
    counter = 0;
    while(sum<m) {
        if(active) {
            sum+=a;
            active=false;
        } else {
            sum+=b;
            active = true;
        }
    }
    if(active) counter++;
    active = true;
    sum = 0;
    while(sum<m) {
        if(active) {
            sum+=c;
            active = false;
        } else {
            sum += d;
            active = true;
        }
    }
    if(active) counter++;
    active = true;
    sum = 0;
    if(counter == 2) cout << "none\n";
    if(counter == 1) cout << "one\n";
    if(counter == 0) cout << "both\n";
    counter = 0;
    while(sum<g) {
        if(active) {
            sum+=a;
            active=false;
        } else {
            sum+=b;
            active = true;
        }
    }
    if(active) counter++;
    active = true;
    sum = 0;
    while(sum<g) {
        if(active) {
            sum+=c;
            active = false;
        } else {
            sum += d;
            active = true;
        }
    }
    if(active) counter++;
    active = true;
    sum = 0;
    if(counter == 2) cout << "none\n";
    if(counter == 1) cout << "one\n";
    if(counter == 0) cout << "both\n";
    counter = 0;
    return 0;
}
