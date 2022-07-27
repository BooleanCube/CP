#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("billboard.in", "r", stdin);
    freopen("billboard.out", "w", stdout);

    int ax1, ay1, ax2, ay2; cin >> ax1 >> ay1 >> ax2 >> ay2;
    int gx1, gy1, gx2, gy2; cin >> gx1 >> gy1 >> gx2 >> gy2;

    int tx1, ty1, tx2, ty2; cin >> tx1 >> ty1 >> tx2 >> ty2;

    int aArea = (ax2-ax1)*(ay2-ay1);
    int gArea = (gx2-gx1)*(gy2-gy1);

    int atx = max(0, min(ax2,tx2) - max(ax1,tx1));
    int aty = max(0, min(ay2,ty2) - max(ay1,ty1));
    int gtx = max(0, min(gx2,tx2) - max(gx1,tx1));
    int gty = max(0, min(gy2,ty2) - max(gy1,ty1));
    
    cout << aArea+gArea-(atx*aty)-(gtx*gty);
}
