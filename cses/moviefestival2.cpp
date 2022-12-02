#include <bits/stdc++.h>
#include <utility>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<pair<int, int>> movies(n);
    multiset<pair<int, int>> start;
    for(int i=0; i<k; i++) start.insert(make_pair(-1, 0));
    for(int i=0; i<n; i++) {
        int a, b;
        cin >> a >> b;
        movies[i] = make_pair(b, a);
    }
    sort(movies.begin(), movies.end());
    int counter = 0;
    int current = 1;
    for(pair<int,int> movie : movies) {
        if(movie.second < current) {
            auto it = start.lower_bound(make_pair(current, 0));
            pair<int, int> p = *(it);
            if(p.first < current) continue;
            counter++;
            current = p.first;
        }
    }
    cout << counter << endl;
}
