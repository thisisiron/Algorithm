#include <cstdio>

int N;

int main() {
	
	scanf("%d", &N);
	
	int count = 0;
	
	while(N!=0){
		if(N%5==0){
			count++;
			N = N-5;		
		}
		else if(N%3==0){
			count++;
			N = N-3;
		}
		else if(N>5){
			count++;
			N = N-5;
		}
		else {
			break;
		}
	}
	if(N!=0) printf("-1");
	else printf("%d\n", count);
	return 0;
}
