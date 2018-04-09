#include <iostream>
#include <deque>
using namespace std;

int visit[30];
deque<int> queue;

void BFS(int Map[][30],int N, int v) {
	
	visit[v] = 1;
	printf("여기서부터 시작 : %d\n", v);
	queue.push_back(v);
	
	while(!queue.empty()){
		
		v = queue.front();
		queue.pop_front();
		
		for(int i=0; i<N ;i++){
			if(Map[v][i] == 1 && !visit[i]){
				visit[i] = 1;
				printf("%d에서 %d로 이동\n", v, i);
				queue.push_back(i);
			}
		}		
		
	}
	
	
}


int main() {
	int N; // 정점의 수 
    int start; // 시작 정점 
    int v1, v2; // 정점과 정점사이의 연결 여부
    
    int Map[30][30]; // 인접 행렬

	scanf("%d %d", &N, &start); 
	
	while(1){
		scanf("%d %d", &v1, &v2);
		if(v1 == -1 && v2 == -1) break;
		Map[v1][v2] = Map[v2][v1] = 1;
	}
    
    BFS(Map, N, start);
    
    return 0;
}
