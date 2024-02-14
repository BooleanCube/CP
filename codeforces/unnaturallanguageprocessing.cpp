#include <iostream>
#include <string>

using namespace std;

int main() {
    int tc;
    cin >> tc;

    while (tc--) {
        int n;
        cin >> n;
        string s;
        cin >> s;

        if (n <= 3) {
            cout << s << endl;
            continue;
        }

        string ans = "";
        for (int i = 0; i < n; ++i) {
            if (s[i] == 'a' || s[i] == 'e') {
                if ((i + 3 < n && (s[i + 3] == 'a' || s[i + 3] == 'e')) || i + 2 == n) {
                    ans += s.substr(i - 1, 3) + ".";
                } else {
                    ans += s.substr(i - 1, 2) + ".";
                }
            }
        }

        cout << ans.substr(0, ans.size() - 1) << endl;
    }

    return 0;
}
