#include <bits/stdc++.h>
using namespace std;

#define ssize(x) (int)(x).size()

int mod;

long long bin_exp(long long b, long long e) {
    assert(0 <= e);
    auto res = 1LL;
    if ((b %= mod) < 0) b += mod;
    for (; e; b = b * b % mod, e /= 2)
        if (e & 1) res = res * b % mod;
    return res;
}

pair<int, long long> row_reduce(vector<vector<long long>>& mat, int cols) {
    auto n = ssize(mat), m = ssize(mat[0]);
    int rank = 0;
    auto det = 1LL;
    assert(cols <= m);
    for (int col = 0; col < cols && rank < n; col++) {
        auto it = find_if(begin(mat) + rank, end(mat), [&](auto & v) {return v[col];});
        if (it == end(mat)) {
            det = 0;
            continue;
        }
        if (it != begin(mat) + rank) {
            det = det == 0 ? 0 : mod - det;
            iter_swap(begin(mat) + rank, it);
        }
        det = det * mat[rank][col] % mod;
        auto a_inv = bin_exp(mat[rank][col], mod - 2);
        for (auto& val : mat[rank]) val = val * a_inv % mod;
        for (int i = 0; i < n; i++)
            if (i != rank && mat[i][col] != 0) {
                auto val = mat[i][col];
                for (int j = 0; j < m; j++) {
                    mat[i][j] -= mat[rank][j] * val % mod;
                    if (mat[i][j] < 0) mat[i][j] += mod;
                }
            }
        rank++;
    }
    return {rank, det};
}

struct matrix_info {
    int rank; /**< max number of linearly independent vectors */
    long long det; /**< determinant */
    vector<long long> x; /**< solution vector, empty iff no solution */
};

matrix_info solve_linear_mod(vector<vector<long long>>& mat, const vector<long long>& b) {
    assert(ssize(mat) == ssize(b));
    auto n = ssize(mat), m = ssize(mat[0]);
    for (auto i = 0; i < n; i++)
        mat[i].push_back(b[i]);
    auto [rank, det] = row_reduce(mat, int(m));
    if (any_of(begin(mat) + rank, end(mat), [](auto & v) {return v.back();})) {
        return {rank, det, {}}; //no solution exists
    }
    vector x(m, 0LL);
    int j = 0;
    for_each(begin(mat), begin(mat) + rank, [&](auto & v) {
        while (v[j] == 0) j++;
        x[j] = v.back();
    });
    return {rank, det, x};
}

typedef long long ll;

int main() {
    int n, m, p;
    cin >> n >> m >> p;

    mod = p;

    int numVariables = n * m;
    int numEquations = n * m;

    vector<vector<ll>> mat(numEquations, vector<ll>(numVariables));
    vector<ll> b(numVariables);

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            int num;
            cin >> num;
            b[i * m + j] = p - num;
            for (int k = 0; k < n; k++)
                mat[i * m + j][k * m + j] = 1;
            for (int k = 0; k < m; k++)
                mat[i * m + j][i * m + k] = 1;
        }
    
    matrix_info ans = solve_linear_mod(mat, b);

    if (ans.x.empty()) {
        cout << -1 << endl;
        return 0;
    }

    int sum = 0, nonzero = 0;
    for (int i = 0; i < numVariables; i++) {
        sum += ans.x[i];
        nonzero += ans.x[i] != 0;
    }

    if (sum > p * m * n) {
        cout << -1 << endl;
        return 0;
    }

    cout << nonzero << endl;
    for (int i = 0; i < numVariables; i++)
        if (ans.x[i] != 0) cout << ans.x[i] << " ";
    cout << endl;




}