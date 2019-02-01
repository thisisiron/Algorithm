#include <cstdio>

int n,m;
int root[1000001];

int _find(int node){
	if(root[node]==node) return node;
	else return root[node] = _find(root[node]);
}

void _union(int a, int b){
	int pa = _find(a);
	int pb = _find(b);
	root[pb] = pa;
}

int main() {
	scanf("%d %d", &n, &m);
	for(int i=0;i<=n;i++) root[i] = i;
	for(int i=0;i<m;i++){
		int a,b,c;
		scanf("%d %d %d", &a,&b,&c);
		if(a==0) {
			_union(b,c);
		} 
		else if(a==1) {
			if(_find(b)==_find(c)) printf("YES\n");
			else printf("NO\n");
		}
	}
	
	return 0;
}
