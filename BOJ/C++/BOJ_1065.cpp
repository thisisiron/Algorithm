#include <cstdio>

int N;
int cnt = 99;

int main(){
	
	scanf("%d", &N);
	
	if(N<100) {
		printf("%d\n", N);
		return 0;
	}
	
	for(int i=100;i<=N;i++){
		int x,y,z;
		x = i / 100;
		y = (i % 100) / 10;
		z = i % 10;
		
		if(x-y == y-z) cnt++; 
		
	}
	
	printf("%d\n", cnt);
	
	
	
	return 0;
}
