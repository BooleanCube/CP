#include <bits/stdc++.h>
using namespace std;

typedef vector<double> vd;
typedef vector<int> vi;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const double eps = 1e-12;

int solveLinear(vector<vd>& A, vd& b, vd& x) {
	int n = sz(A), m = sz(x), rank = 0, br, bc;
	if (n) assert(sz(A[0]) == m);
	vi col(m); iota(all(col), 0);

	rep(i,0,n) {
		double v, bv = 0;
		rep(r,i,n) rep(c,i,m)
			if ((v = fabs(A[r][c])) > bv)
				br = r, bc = c, bv = v;
		if (bv <= eps) {
			rep(j,i,n) if (fabs(b[j]) > eps) return -1;
			break;
		}
		swap(A[i], A[br]);
		swap(b[i], b[br]);
		swap(col[i], col[bc]);
		rep(j,0,n) swap(A[j][i], A[j][bc]);
		bv = 1/A[i][i];
		rep(j,i+1,n) {
			double fac = A[j][i] * bv;
			b[j] -= fac * b[i];
			rep(k,i+1,m) A[j][k] -= fac*A[i][k];
		}
		rank++;
	}

	x.assign(m, 0);
	for (int i = rank; i--;) {
		b[i] /= A[i][i];
		x[col[i]] = b[i];
		rep(j,0,i) b[j] -= A[j][i] * b[i];
	}
	return rank;
}

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {-1, -1, 1, 1};

bool valid(int row, int col, int n) {
    return row >= 0 && row < n && col >= 0 && col <= row;
}

int getId(int row, int col) {
    return row*(row+1)/2 + col;
}

int main() {
    int n; cin >> n;
    int H = n*(n+1)/2;
    vector<vd> mat(H, vd(H)), p(H, vd(5));
    vd b(H), x(H);
    vi c(H);
    for(int i=0; i<H; i++) cin >> c[i];
    for(int i=0; i<H; i++)
        for(int j=0; j<5; j++)
            cin >> p[i][j];
    for(int i=0; i<n; i++) {
        for(int j=0; j<=i; j++) {
            int id = getId(i, j);
            for(int k=0; k<4; k++) {
                int x = i+dy[k], y = j+dx[k];
                if(!valid(x, y, n)) continue;
                mat[id][getId(x, y)] += p[id][k];
            }
            mat[id][id] = -1;
            b[id] = -p[id][4]*c[id];
        }
    }
    solveLinear(mat, b, x);
    cout << fixed << setprecision(10) << x[0] << endl;
    return 0;
}