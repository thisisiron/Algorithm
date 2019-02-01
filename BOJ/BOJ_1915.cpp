#include <cstdio>

int n,m;
int map[1001][1001];
int D[1001][1001];

int min(int a, int b) {
	return (a>b)?b:a;
}

int max(int a, int b) {
	return (a>b)?a:b;
}

int main() {
	scanf("%d %d", &n, &m);
	
	for(int i=1;i<=n;i++){
		for(int j=1;j<=m;j++){
			scanf("%1d", &map[i][j]);
		}
	}
	
	int answer = 0;
	
	for(int i=1;i<=n;i++){
		for(int j=1;j<=m;j++){
			if(map[i][j]==0) D[i][j]=0;
			else {
				D[i][j] = min(D[i][j-1], D[i-1][j]);
				D[i][j] = min(D[i][j], D[i-1][j-1]) + 1;
				answer = max(answer, D[i][j]);
			}
		}
	}
	
	
	printf("%d", answer*answer);
	
	return 0;
}
