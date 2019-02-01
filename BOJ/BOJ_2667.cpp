#include <cstdio>
#include <algorithm>

using namespace std;

int N;
int map[25][25];
int dir[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};
int cnt;
int answer[25*25];

void dfs(int i, int j, int &answer) {
	map[i][j] = 0;
	answer++;
	
	for(int k=0;k<4;k++){
		int ii = i + dir[k][0];
		int jj = j + dir[k][1];
		
		if(ii<0||jj<0||ii>=N||jj>=N) continue;
		
		if(map[ii][jj]==0) continue;
		
		dfs(ii,jj,answer);	
	}
	
}


int main() {
	scanf("%d",&N);
	
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			scanf("%1d", &map[i][j]);
		}
	}
	
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			if(map[i][j]==1){
				dfs(i,j,answer[cnt]);
				cnt++;
			}
		}
	}
	
	printf("%d\n", cnt);
	
	sort(answer, answer+cnt);
	
	for(int i=0;i<cnt;i++){
		printf("%d\n", answer[i]);
	}
	
	
	return 0;
}
