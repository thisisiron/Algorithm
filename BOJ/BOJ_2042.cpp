#include <cstdio>

int n,m,k;
long long tree[1000000*4];

int init() {
	for(int i=0;i<n*4;i++) tree[i] = 0;
	int ret = 1;
	while(ret<n) ret *= 2;
	ret--;
	return ret;
}

void update(int idx, long long data) {
	int cur = idx;
	while(cur > 0){
		tree[cur] += data;
		cur/=2;
	}
}

long long sum(int start, int end) {
	long long ret = 0;
	while(start<=end){
		if(start%2==1) ret += tree[start];
		if(end%2==0) ret += tree[end];
		start = (start+1) / 2;
		end = (end-1) / 2;	
	}

	return ret;
}

int main() {
	
	scanf("%d %d %d", &n, &m, &k);
	
	// Calculating a index of data and Initializing tree 
	int Nidx = init();
	
	for(int i=1; i<=n; i++){
		scanf("%lld", &tree[Nidx+i]);
	}
	
	// Creating a tree
	for(int i=Nidx;i>=0;i--) tree[i] = tree[i*2] + tree[i*2 + 1];
	
	for(int i=0; i<m+k;i++){
		int a, b, c;
		scanf("%d %d %d", &a, &b, &c);
		if(a==1) {
			update(Nidx+b, (long long)c-tree[Nidx+b]);
		}
		else if(a==2){
			printf("%lld\n", sum(Nidx+b, Nidx+c));
		}
	}
	
	return 0;
}
