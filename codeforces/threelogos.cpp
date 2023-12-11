#include <bits/stdc++.h>
using namespace std;

bool tryPattern1(vector<int>& x, vector<int>& y, vector<char>& l){
	if(x[0] == x[1] && x[1] == x[2] && x[2] == y[0]+y[1]+y[2]){
		cout << x[0] << "\n";
		for(int logo=0; logo < 3; logo++){
			for(int r=0; r < y[logo]; r++){
				for(int c=0; c < x[logo]; c++){
					cout << l[logo];
				}
				cout << "\n";
			}
		}
		return true;
	}
	return false;
}

bool tryPattern2(vector<int>& x, vector<int>& y, vector<char>& l){
	if(x[0]+x[1] == x[2] && y[0] == y[1] && x[2] == y[0]+y[2]){
		cout << x[2] << "\n";
		for(int r=0; r < y[0]; r++){
			for(int c1=0; c1 < x[0]; c1++){
				cout << l[0];
			}
			for(int c2=0; c2 < x[1]; c2++){
				cout << l[1];
			}
			cout << "\n";
		}
		for(int r=0; r < y[2]; r++){
			for(int c=0; c < x[2]; c++){
				cout << l[2];
			}
			cout << "\n";
		}
		return true;
	}
	return false;
}

int main() {
	vector<int> xlen(3), ylen(3);
	for(int i=0; i<3; i++) cin >> xlen[i] >> ylen[i];

	vector<int> position = {0, 1, 2};
	vector<char> logos = {'A', 'B', 'C'};
	int ans = -1;

	do{
		for(int mask=0; mask<(1 << 3); mask++){
			vector<int> xrotate(3), yrotate(3);
			for(int pos=0; pos<3; pos++)
			{
				if(mask & (1 << pos)){
					xrotate[pos] = ylen[pos];
					yrotate[pos] = xlen[pos];
				}
				else{
					xrotate[pos] = xlen[pos];
					yrotate[pos] = ylen[pos];
				}
			}
			vector<int> xdisp(3), ydisp(3);
			vector<char> newlogos(3);
			for(int i=0; i<3; i++){
				xdisp[i] = xrotate[position[i]];
				ydisp[i] = yrotate[position[i]];
				newlogos[i] = logos[position[i]];
			}

			if(tryPattern1(xdisp, ydisp, newlogos)){
				ans = xdisp[0];
				return 0;
			}
			if(tryPattern2(xdisp, ydisp, newlogos)){
				ans = xdisp[2];
				return 0;
			}
		}
	}while(next_permutation(position.begin(), position.end()));
	
	if(ans == -1) cout << ans;
	return 0;
}
