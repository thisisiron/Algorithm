#include <cstdio>
#include <stack>
using namespace std;

int T;
int m,n,k;
int map[50][50];
int dir[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
int answer;
stack<pair<int, int > > s;

//void dfs(int i, int j){
//	map[i][j] = 0;
//	
//	for(int k=0;k<4;k++){
//		int ii = i + dir[k][1];
//		int jj = j + dir[k][0];
//	
//		if(ii<0||jj<0||ii>=n||jj>=m) continue;
//	
//		if(map[ii][jj]==0) continue;
//		
//		dfs(ii,jj);
//	
//	}
//}

void dfs_stack(int i, int j){
	s.push({i, j});
	
	while(!s.empty()){
		pair<int,int> pos = s.top();
		i = pos.first;
		j = pos.second;
		map[i][j] = 0;
		s.pop();
		for(int k=0;k<4;k++){
			int ii = i + dir[k][1];
			int jj = j + dir[k][0];
			if(ii<0||jj<0||ii>=n||jj>=m) continue;
			if(map[ii][jj]==0) continue;
			s.push({ii,jj});
			
		}
	}
	
}


int main(){
	
	scanf("%d", &T);
	
	while(T--){
		answer = 0;
		scanf("%d %d %d", &m,&n,&k);
		for(int i=0;i<k;i++){
			int x,y;
			scanf("%d %d", &x,&y);
			map[y][x] = 1;
		}
		
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if(map[i][j]==1){
//					dfs(i,j);
					dfs_stack(i,j);
					answer++;
				}
			}
		}
		printf("%d\n",answer);
	}
	
	return 0;
}
