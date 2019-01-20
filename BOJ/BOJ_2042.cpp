#include <cstdio>

int n,m,k;
int arr[1000001];
int main() {
	
	scanf("%d %d %d", &n, &m, &k);
	
	for(int i=1; i<=n; i++){
		int x;
		scanf("%d", &x);
		arr[i] = x;
	}
	
	for(int i=0; i<m+k;i++){
		int a, b, c;
		scanf("%d %d %d", &a, &b, &c);
		if(a==1) {
			arr[b] = c;
		}
		else if(a==2){
			
		}
	}
	
	return 0;
}
