#include <bits/stdc++.h>
using namespace std;

int idxOfLowestEven(int a[], int n) {
    int min = 16;
    int idx = -1;
    for(int i=0; i<n; i++) {
        if(a[i] < min && a[i] % 2 == 0) {
            min = a[i];
            idx = i;
        }
    }
    return idx;
}

int idxOfMax(int a[], int n) {
    int max = 0;
    int idx = 0;
    for(int i=0; i<n; i++) {
        if(a[i] > max) {
            max = a[i];
            idx = i;
        }
    }
    return idx;
}

int findSum(int a[], int n) {
    int sum = 0;
    for(int i=0; i<n; i++) sum += a[i];
    return sum;
}

int main() {
    int t; cin >> t;
    for(int i=0; i<t; i++) {
        int n; cin >> n;
        int *arr[n];
        for(int j=0; j<n; j++) cin >> *arr[j];
        int prevSum = 0;
        while(prevSum < findSum(*arr, n)) {
            prevSum = findSum(*arr, n);
            int idxMin = idxOfLowestEven(*arr, n);
            if(idxMin < 0) break;
            int idxMax = idxOfMax(*arr, n);
            *arr[idxMin] = (int) *arr[idxMin]/2;
            *arr[idxMax] = (int) *arr[idxMax]*2;
        }
        cout << prevSum << endl;
    }
    return 0;
}
