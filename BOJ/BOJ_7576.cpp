#include <cstdio>
#include <queue>
using namespace std;

int m,n;
int tomatos[1000][1000];
queue<pair<int, int> > q;
int dir[4][2] = {{0,-1},{0,1},{1,0},{-1,0}};
int cnt;
int answer = 1;

int bfs() {
	
	while(!q.empty()){

		int size = q.size();
		
        for (int j= 0; j< size; j++) {
        	
        	int a = q.front().first;
			int b = q.front().second;
			
			q.pop();
			
        	for(int i=0;i<4;i++){
				int aa = a - dir[i][0];
				int bb = b - dir[i][1];
				
				
				if(aa<0 || bb<0 || aa>=n || bb>=m ) continue;
				else if(tomatos[aa][bb] == -1 || tomatos[aa][bb] == 1) {
					continue; // 토마토가 없거나 이미 익은 경우 
				}
				else if(tomatos[aa][bb]==0) { 
					cnt--;
					q.push({aa,bb});
					tomatos[aa][bb] = 1;
				}
				
				if(cnt==0) return answer;	
			}	
        }

		answer++;
		
	}
	
	return -1;
	
}

int main() {
	
	scanf("%d %d", &m, &n);
	
	
	for(int i=0;i<n;i++) {
		for(int j=0;j<m;j++) {
			scanf("%d", &tomatos[i][j]);
			
			if(tomatos[i][j]==1){
				q.push({i,j});
			}
			else if(tomatos[i][j]==0){
				cnt++;	
			}
		}
	}

	if(cnt==0) printf("0");
	else printf("%d\n", bfs());
	
	
	
	return 0;
}
