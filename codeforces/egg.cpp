#include <bits/stdc++.h>
#define INFTY 1e18L
using namespace std;
using ll = long long;
ll DP(vector<vector<ll>> &vec, vector<vector<vector<ll>>> &dp, int i, int f, int s){
    if(i >= vec.size()) return 0;
    if(f == 0 && s == 0) return 0;
    if(dp[i][f][s] != 0) return dp[i][f][s];
    ll ans = DP(vec, dp, i+1, f, s);
    if(f) ans = max(ans, DP(vec, dp, i+1, f-1, s) + vec[i][0]);
    if(s) ans = max(ans, DP(vec, dp, i+1, f, s-1) + vec[i][1]);
    return dp[i][f][s] = ans;
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int N,F,S;
    cin>>N>>F>>S;
    vector<vector<ll>> satisfactions;
    for(int i=0;i<N;++i){
        ll f,s;
        cin>>f>>s;
        satisfactions.push_back({f,s});
    }
    vector<vector<vector<ll>>> dp(N, vector<vector<ll>>(F+1, vector<ll>(S + 1)));
    cout<< DP(satisfactions, dp, 0, F, S) << '\n';
    return 0;
}
