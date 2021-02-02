#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int nums[2];
    cin >> nums[0] >> nums[1];
    int res = round(nums[0] / pow(10, nums[1]));
    int resu = res*static_cast<int>(round(pow(10, nums[1])));
    cout << resu;
    return 0;
}
