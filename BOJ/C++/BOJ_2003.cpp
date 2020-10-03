#include <cstdio>

int n, m;
int arr[10000];
int count;

int main() {
	scanf("%d %d", &n, &m);
	
	for(int i=0;i<n;i++){
		scanf("%d", &arr[i]);
	}
	
	int sum;
	for(int i=0;i<n;i++){
		sum = 0;
		for(int j=i;j<n;j++){
			sum += arr[j];	
			if(sum == m) count++;
		}
	}
	
	printf("%d", count);
	
	return 0;
}
