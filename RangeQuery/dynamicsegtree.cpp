//you can just use long long, i was playing around with stdint.h
//segment tree

#include <iostream>
#include <vector>
#include <stdint.h>
using namespace std;

//O(nlogn)
//this basically just does updateNode() n times so this method was entirely unecessary
void constructTree(vector<uint64_t>* nums, uint64_t a) {
	for(uint64_t i=a; i<=2*a; i++) {
		uint64_t b = i;
		while(b>1) {
			b>>=1;
			nums->at(b) += nums->at(i);
		}
	}
}

//O(logn)
void updateNode(vector<uint64_t>* nums, uint64_t k, uint64_t w) {
	uint64_t v = nums->at(k);
  	uint64_t b = k;
	nums->at(k) = w;
	while(b>1) {
		b>>=1;
		nums->at(b) -= v;
		nums->at(b) += w;
	}
}

//O(logn)
uint64_t getSumRange(vector<uint64_t>* nums, uint64_t k, uint64_t w, uint64_t sum) {
	if(k == w) return nums->at(k) + sum;
	if(k%2 == 1) { sum += nums->at(k); k++; }
	if(k == w) return nums->at(k) + sum;
	if(w%2 == 0) { sum += nums->at(w); w--; }
 	return getSumRange(nums, k>>1, w>>1, sum);
}

int main() {
	uint64_t a, b; cin >> a >> b;
	vector<uint64_t>* nums = new vector<uint64_t>(2*a+1, 0);
	for(uint64_t i=0; i<a; i++) cin >> nums->at(a+i);
	constructTree(nums, a);
	for(uint64_t i=0; i<b; i++) {
		uint64_t q, k, w; cin >> q >> k >> w;
		if(q == 1) updateNode(nums, a+k-1, w);
		else cout << getSumRange(nums, a+k-1, a+w-1, 0) << endl;
	}
}
