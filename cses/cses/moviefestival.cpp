// not intuitive but it works

#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    int n; cin >> n;
    vector<pair<int, int>>* movies = new vector<pair<int, int>>;
    for(int i=0; i<n; i++) {
        int a, b; cin >> a >> b;
        movies->push_back(pair<int,int>(b,a));
    }
    sort(movies->begin(), movies->end());
    int counter = 0;
    int current = 1;
    for(pair<int, int> movie : *movies) {
        if(movie.second < current) continue;
        ++counter;
        current = movie.first;
    }
    cout << counter << endl;
    return 0;
}

