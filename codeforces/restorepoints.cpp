#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> tri;
multiset<int> options;
bool done = 0;

void backtrack(int dep, int n) {
    if(done) return;
    if(dep >= n-1) {
        done = 1;
        return;
    }
    tri[dep] = vector<int>(dep+1);
    vector<int> cur;
    for(int i=1; i<dep; i++) {
        tri[dep][i] = tri[dep-1][i-1]+tri[dep-1][i]-tri[dep-2][i-1];
        if(options.count(tri[dep][i]) == 0) {
            for(int addback : cur) options.insert(addback);
            return;
        }
        cur.emplace_back(tri[dep][i]);
        options.erase(options.find(tri[dep][i]));
    }
    int a = *(--options.end()), b = *(--(--options.end()));
    if(dep == n-2) {
        tri[dep][0] = a; tri[dep][dep] = b;
        if(tri[dep][1]+tri[dep][0] != tri[dep-1][0] || tri[dep][dep]+tri[dep][dep-1] != tri[dep-1][dep-1]) {
            swap(tri[dep][0], tri[dep][dep]);
            if(tri[dep][1]+tri[dep][0] != tri[dep-1][0] || tri[dep][dep]+tri[dep][dep-1] != tri[dep-1][dep-1]) {
                return;
            }
        }
        backtrack(dep+1, n);
        return;
    }
    options.erase(options.find(a));
    options.erase(options.find(b));
    tri[dep][0] = a; tri[dep][dep] = b;
    backtrack(dep+1, n);
    swap(tri[dep][0], tri[dep][dep]);
    backtrack(dep+1, n);
}

int main() {
    int tc; cin >> tc;
    while(tc--) {
        done = 0;
        int n; cin >> n;
        int m = n*(n-1)/2;
        vector<int> nums(m);
        options = multiset<int>();
        for(int i=0; i<m; i++) {
            cin >> nums[i];
            options.insert(nums[i]);
        }
        sort(nums.begin(), nums.end());
        if(n == 2) {
            cout << "0 " << nums[0] << endl;
            continue;
        }
        tri = vector<vector<int>>(n);
        tri[0].emplace_back(nums[m-1]);
        tri[1].emplace_back(nums[m-2]);
        tri[1].emplace_back(nums[m-3]);
        options.erase(options.find(tri[0][0]));
        options.erase(options.find(tri[1][0]));
        options.erase(options.find(tri[1][1]));
        backtrack(2, n);
        int s = 0;
        cout << "0 ";
        for(int i=0; i<n-1; i++) {
            s += tri[n-2][i];
            cout << s << " \n"[i == n-2];
        }
    }
    return 0;
}
