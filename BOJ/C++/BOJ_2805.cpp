#include <cstdio>

int n, m;
int trees[1000001];
int mx;

int max(int a, int b){
	return (a>b)?a:b;
}

long long cutting(int h) {
	long long sum = 0;
	for(int i=0;i<n;i++){
		if(trees[i]>h) sum += trees[i] - h;
	}
	return sum;
}


int main() {
	
	scanf("%d %d", &n, &m);
	
	for(int i=0;i<n;i++){
		scanf("%d", &trees[i]);
		mx = max(mx, trees[i]);
	}
	
	int left = 0;
	int right = mx;
	long long temp;
	int ans;
	
	while(left<right){
		int mid = (left+right) / 2;
		
		temp = cutting(mid);
		if(temp < m){
			right = mid;
		} else {
			ans = mid;
			left = mid + 1;
		}
		
	}
	
	printf("%d", ans);
	
	
	return 0;
}
