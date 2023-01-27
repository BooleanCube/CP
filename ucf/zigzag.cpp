#include <bits/stdc++.h>
#include <utility>
using namespace std;

vector<pair<int, string>> palindromes(string s) {
    int len = s.size();
    vector<vector<bool>> dp(len, vector<bool>(len,0));
    for(int i=0; i<len; i++) {
        dp[i][i] = 1;
        if(i<len-1 && s[i] == s[i+1]) dp[i][i+1] = 1;
    }
    for(int i=3; i<=len; i++)
        for(int j=0; len<j+i-1; j++)
            if(s[j] == s[j+i-1] && dp[j+1][j+len-2]) dp[j][j+len-1] = 1;
    vector<int> p(len,0);
    for(int i=0; i<len; i++) {
        int j=0;
        int k=1;
        while(k+i<len) {
            if(s[j+i]==s[k+i]) {
                dp[k+i-j][k+i]=0;
                p[k] = j+1;
                j++;
                k++;
            }
            else if(j>0) j=p[j-1];
            else {
                p[k]=0;
                k++;
            }
        }
    }
    vector<pair<int, string>> *result = new vector<pair<int, string>>;
    int count = 0;
    for (int i=0; i<len; i++) {
        string str;
        for (int j=i; j<len; j++) {
            str += s[j];
            if(dp[i][j]) {
                count++;
                result->push_back(make_pair(str.size(), str));
            }
        }
    }
    return *result;
}

int main() {

}
