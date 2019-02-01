#include <cstdio>

int N;
int count;
bool isPrime(int n) {
	if(n<=1) return false;
	for(int i=2;i*i<=n;i++) { // root n까지만 확인하면 된다.
		if(n%i==0) return false;
	}
	return true;
}

int main() {
	
	scanf("%d", &N);
	
	int num;
	for(int i=0;i<N;i++){
		
		scanf("%d", &num);
		if(isPrime(num)){
			count++;
		}
		
	}

	printf("%d\n", count);
	
	
	return 0;
}
