#include <iostream>
using namespace std;

int main() {
    int arr[26] = {2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9};
    int n; string in;
    cin >> n;
    string dic[n];
    for(int x=0; x<n; x++) cin >> dic[x];
    cin >> in;
    int counter = 0;
    for(int x=0; x<n; x++) {
        if(dic[x].length() != in.length())
            continue;
        string word = dic[x];
        bool cube = true;
        for(int a=0; a<in.length(); a++)
            if(arr[word[a] - 'a'] != in[a] - '0') {
                cube = false;
                break;
            }
        if(cube) ++counter;
    }
    cout << counter;
    return 0;
}
