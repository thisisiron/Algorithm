#include <cstdio>

int n,m;
int arr[51];
int cnt;

int main() {
	scanf("%d %d", &n, &m);
	
	for(int i=1;i<=n;i++) {
		arr[i] = i;
	}
	
	for(int i=1;i<=m;i++) {
		int val;
		scanf("%d",&val);
	}
	
	return 0;
}
