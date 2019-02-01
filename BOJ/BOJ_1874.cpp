#include <cstdio>

int n;
int arr[100001];
int val[100001];
int top;

int main() {
	
	scanf("%d", &n);
	
	for(int i=0;i<n;i++){
		scanf("%d", &val[i]);
	}
	
	for(int i=1;i<=n;i++){
		arr[i] = i;
	}
	
	
	
	return 0;
}
