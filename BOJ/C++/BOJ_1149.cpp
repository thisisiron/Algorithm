#include <cstdio>
#define INF 1001
int n;
int rgb[1001][3];
int D[1001][3];

int min(int a, int b) {
	return (a>b)?b:a;
}

int main() {
	scanf("%d", &n);
	
	for(int i=1; i<=n; i++){
		scanf("%d %d %d", &rgb[i][0], &rgb[i][1], &rgb[i][2]);
	}
	
	
	for(int i=1;i<=n;i++){
		D[i][0] += rgb[i][0] + min(D[i-1][1],D[i-1][2]);
		D[i][1] += rgb[i][1] + min(D[i-1][0],D[i-1][2]);
		D[i][2] += rgb[i][2] + min(D[i-1][0],D[i-1][1]);
	}
	int mn = min(D[n][0],D[n][1]);	
	mn = min(mn, D[n][2]);
	printf("%d", mn);
	
	return 0;
}

/*
3
5 5 5
6 6 1
5 6 7

*/
