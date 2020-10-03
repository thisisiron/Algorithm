#include <cstdio>

int self_number(int N) {
	int res = N;
	if(N>=10000) {
		res += N / 10000;
		N %= 10000;
	}
	if(N>=1000) {
		res += N / 1000;
		N %= 1000;
	}
	if(N>=100) {
		res += N / 100;
		N %= 100;
	}
	if(N>=10) {
		res += N / 10;
		N %= 10;
	}
	res += N;
	
	return res;

}

int d[10001];
int main() {
	for(int i=1; i<=10000; i++){
		d[self_number(i)] = 1;
		if(d[i]==0) printf("%d\n", i);
	}
	
	
	return 0;
}
