#include <cstdio>

int N;
int D[1000001];

int min(int a, int b) {
	return a>b?b:a;
}

int main() {
	
	scanf("%d", &N);
	// D는 i까지 가는데 최소한의 수 
	for(int i=2;i<=N;i++){
		D[i] = D[i-1] + 1;
		if(i%3==0) D[i] = min(D[i], D[i/3] + 1);
		if(i%2==0) D[i] = min(D[i], D[i/2] + 1);
	}
	
	printf("%d", D[N]);
	
	return 0;
}
