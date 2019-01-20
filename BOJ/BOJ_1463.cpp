#include <cstdio>

int N;
int count;

int main() {
	
	scanf("%d", &N);
	
	while(N>1){
		if(N%3==1) N = N - 1;
		else if(N%3==0) N = N/3;
		else if(N%2==0) N = N/2;s
		count++;
	}
	printf("%d", count);	
	
	return 0;
}
