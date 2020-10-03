#include <cstdio>


int main() {
	int n;
	scanf("%d", &n);
	long long a = 0;
	long long b = 1;
	long long c = 1;
	for(int i=0;i<n-1;i++){
		c = a+b;
		a = b;
		b = c;
	}
	
	printf("%lld", c);
	
	
	return 0;
}
