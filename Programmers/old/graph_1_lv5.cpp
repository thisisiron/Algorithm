#include <string>
#include <vector>
#include <set>
using namespace std;

int dx[8] = {0, 1, 1, 1, 0, -1, -1, -1};
int dy[8] = {1, 1, 0, -1, -1, -1, 0, 1};

set<pair<int, int>> vertex;
set<pair<pair<int, int>, pair<int, int>>> edge;

int solution(vector<int> arrows) {
    int answer = 0;
    
    vertex.insert({0,0});
    int x=0, y=0;
    for(int a : arrows){
    	for(int i=0;i<2;i++) {
		
	    	int nx = x + dx[a];
	    	int ny = y + dy[a];
	    	printf("%d %d\n", nx, ny);
	    	pair<int, int> fir = {x,y};
	    	pair<int, int> sec = {nx,ny};
	    	
	    	vertex.insert(sec);
			if(fir>sec) swap(fir,sec); // (1,2)->(1,3) 이나 (1,3)->(1,2)는 같은 Edge 
	    	edge.insert({fir, sec});
	    	
	    	
	    	x = nx;
	    	y = ny;
    	}
	}
    
    answer = edge.size() - vertex.size() + 1;
    printf("%d\n", answer);
    return answer;
}


vector<int> param{6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0};

int main() {
	solution(param);
	
	return 0;
}
