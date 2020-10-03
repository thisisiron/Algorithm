#include <cstdio>

int N,K;
bool isPrime[1001];

int main() {
	
	scanf("%d %d", &N, &K);
	
	isPrime[0] = isPrime[1] = false;
	for(int i=2;i<=N;i++) isPrime[i] = true;
	
	int answer = -1;
	
	for(int i=2;i<=N;i++){
		if(isPrime[i]==false) continue;
		for(int j=i;j<=N;j+=i){
			if(isPrime[j]==false) continue;
			isPrime[j] = false;
			K--;
			if(K==0) answer = j; 
		}
		if(K==0) break;
	}
	
	printf("%d\n", answer);
	
	return 0;
}
