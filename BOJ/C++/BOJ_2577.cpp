#include <cstdio>

int A, B, C;
int answer[10];

int main() {
	scanf("%d", &A);	
	scanf("%d", &B);
	scanf("%d", &C);
	
	A *= B * C;
	
	while(A!=0){
		answer[A%10]++;
		A /= 10;
	}
	
	for(int i=0;i<10;i++){
		printf("%d\n", answer[i]);
	}
	
	return 0;
}
