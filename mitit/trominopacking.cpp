#include <bits/stdc++.h>
using namespace std;
using ll = long long;

void backtrack(int i, int j, int n, int m) {
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;
    vector<vector<vector<int>>> choices{ {{0,-1},{1,0}}, {{0,-1},{-1,0}}, {{0,1},{-1,0}}, {{0,1},{1,0}} };
    for(int i=0;i<t;++i){
        int n,m;
        cin>>n>>m;
        vector<vector<char>> grid(n,vector<char>(m,0));
        vector<vector<bool>> vis(n, vector<bool>(m, 0));
        for(int j=0;j<n;++j){
            string s;
            cin>>s;
            for(int k=0;k<m;++k){
                grid[j][k] = s[k];
            }
        }
        ll ans = 1;
        ll mod = 1000000007;
        for(int j=0;j<n;++j){
            for(int k=0;k<m;++k){
                if(vis[j][k]) continue;
                if(grid[j][k]!='o') continue;
                int bj = j;
                while(grid[bj][k] == 'o' && bj<m) vis[bj++][k] = 1;
                bj--;
                ll c = 0;
                for(auto &choice:choices){
                    bool good = true;
                    for(auto &direction:choice){
                        int x = j + direction[0];
                        int y = k + direction[1];
                        good = good && (x >= 0 && x < n && y >= 0 && y < m && grid[x][y] == '.');
                    }
                    c += good;
                }
                ans = (ans * c) % mod;
                if(bj > j) {
                    c = 0;
                    for(auto &choice:choices){
                        bool good = true;
                        for(auto &direction:choice){
                            int x = bj + direction[0];
                            int y = k + direction[1];
                            good = good && (x >= 0 && x < n && y >= 0 && y < m && grid[x][y] == '.');
                        }
                        c += good;
                    }
                    ans = (ans * c) % mod;
                }
            }
        }
        cout<<ans<<endl;
    }
}
