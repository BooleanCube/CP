#include <bits/stdc++.h>
using namespace std;

struct node {
    int val, m = 0, cnt = 0;
    vector<node*> children;
    node(int val, int m) {
        this->val = val; this->m = m;
        this->children = vector<node*>(m+1, nullptr);
    }
    void insert(vector<int> &perm, int idx) {
        this->cnt++;
        int val = perm[idx];
        if(this->children[val] == nullptr) this->children[val] = new node(val, this->m);
        if(idx == m-1) return;
        this->children[val]->insert(perm, idx+1);
    }
    void remove(vector<int> &perm, int idx) {
        this->cnt--;
        int val = perm[idx];
        if(idx == m-1) return;
        this->children[val]->insert(perm, idx+1);
    }
    int largest(vector<int> &perm, int idx) {
        int val = perm[idx];
        if(this->children[val] == nullptr || idx == m-1) return 1;
        if(this->children[val]->cnt <= 0) return 0;
        return 1 + this->children[val]->largest(perm, idx+1);
    }
};

int main() {
    int tc; cin >> tc;
    while(tc--) {
        int n, m; cin >> n >> m;
        node trie(-1, m);
        vector<vector<int>> perms(n, vector<int>(m));
        for(int i=0; i<n; i++) {
            for(int &j : perms[i]) cin >> j;
            trie.insert(perms[i], 0);
        }
        vector<int> ans(n);
        for(int i=0; i<n; i++) {
            trie.remove(perms[i], 0);
            vector<int> inv(m);
            for(int j=0; j<m; j++) inv[perms[i][j]-1] = j+1;
            // for(int j=0; j<m; j++) cout << perms[i][j] << " \n"[j==m-1];
            // for(int j=0; j<m; j++) cout << inv[j] << " \n"[j==m-1];
            ans[i] = trie.largest(inv, 0);
            trie.insert(perms[i], 0);
        }
        for(int i=0; i<n; i++) cout << ans[i] << " \n"[i==n-1];
    }
    return 0;
}