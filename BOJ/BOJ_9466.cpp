#include <cstdio>

int T, N;
int student[100001];
int visited[100001], finished[100001];
int cnt;

void dfs(int curr) {
	visited[curr] = 1; // visited = 1
	
	int next = student[curr];
	
	if(visited[next]==1){
		if(finished[next]==0) {
			for(int i=next;i!=curr;i=student[i]) {
				cnt++;
			}
			cnt++;
		}
	}
	else dfs(next);
	
	finished[curr] = 1; // finish visiting last vertex 
	
}


int main() {
	scanf("%d", &T);
	
	while(T--){
		cnt = 0;
		
		scanf("%d", &N);

		for(int i=1;i<=N;i++){
			scanf("%d", &student[i]);
			visited[i] = 0;
			finished[i] = 0;
		}
		
		for(int i=1;i<=N;i++){
			if(visited[i]==0) dfs(i);	
		}
		
		printf("%d\n", N-cnt);
		
	}
	
	return 0;
}
