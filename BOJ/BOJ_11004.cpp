#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;


int main() {
	int N, k;
	int input;
	deque<int> d;
	scanf("%d %d", &N, &k);
	while(N--){
		scanf("%d", &input);
		d.push_back(input);
	}
	nth_element(d.begin(), d.begin()+k-1, d.end());
	printf("%d", d[k-1]);

	return 0;
}
