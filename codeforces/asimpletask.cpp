#include <bits/stdc++.h>
using namespace std;

#define ll long long
typedef vector<int> vi;

const int inf = 1e9;
struct Node {
	Node *l = 0, *r = 0;
	int lo, hi, mset = inf, madd = 0, val = -inf;
	Node(int lo,int hi):lo(lo),hi(hi){} // Large interval of -inf
	Node(vi& v, int lo, int hi) : lo(lo), hi(hi) {
		if (lo + 1 < hi) {
			int mid = lo + (hi - lo)/2;
			l = new Node(v, lo, mid); r = new Node(v, mid, hi);
			val = max(l->val, r->val);
		}
		else val = v[lo];
	}
	int query(int L, int R) {
		if (R <= lo || hi <= L) return -inf;
		if (L <= lo && hi <= R) return val;
		push();
		return max(l->query(L, R), r->query(L, R));
	}
	void set(int L, int R, int x) {
		if (R <= lo || hi <= L) return;
		if (L <= lo && hi <= R) mset = val = x, madd = 0;
		else {
			push(), l->set(L, R, x), r->set(L, R, x);
			val = max(l->val, r->val);
		}
	}
	void add(int L, int R, int x) {
		if (R <= lo || hi <= L) return;
		if (L <= lo && hi <= R) {
			if (mset != inf) mset += x;
			else madd += x;
			val += x;
		}
		else {
			push(), l->add(L, R, x), r->add(L, R, x);
			val = max(l->val, r->val);
		}
	}
	void push() {
		if (!l) {
			int mid = lo + (hi - lo)/2;
			l = new Node(lo, mid); r = new Node(mid, hi);
		}
		if (mset != inf)
			l->set(lo,hi,mset), r->set(lo,hi,mset), mset = inf;
		else if (madd)
			l->add(lo,hi,madd), r->add(lo,hi,madd), madd = 0;
	}
};

int main() {
    int n, q; cin >> n >> q;
    string s; cin >> s;
    Node tree(0, n+2);
    for(int t=0; t<q; t++) {
        int i, j, k; cin >> i >> j >> k;
        tree.set(i-1, j, k+1);
    }
    for(int i=0; i<=n; i++) {
        cout << i << " " << tree.query(i, i+1) << endl;
    }
    int pIdx = 0, pVal = tree.query(0, 1);
    for(int i=1; i<n; i++) {
        int val = tree.query(i, i+1);
        if(val != pVal) {
            if(pVal) {
                if(pVal == 1) sort(s.begin()+pIdx, s.end()+(i-1), greater<int>());
                if(pVal == 2) sort(s.begin()+pIdx, s.end()+(i-1));
            }
            pVal = val; pIdx = i;
        }
    }
    cout << s << endl;
    return 0;
}