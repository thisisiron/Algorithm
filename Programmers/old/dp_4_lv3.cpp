#include <string>
#include <vector>

using namespace std;

int map[101][101];
int D[101][101];

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    
    for(vector<int> v: puddles){
    	map[v[1]][v[0]] = -1;
	}
    
    D[0][1] = 1;
    for(int i=1;i<=n;i++) {
    	for(int j=1;j<=m;j++) {
    		if(map[i][j]==-1){
    			D[i][j] = 0;
			}
			else {
				D[i][j] = (D[i][j-1] + D[i-1][j]) % 1000000007;
			}
		}
	}
	
	answer = D[n][m];
    
    return answer;
}

vector<vector<int>> param{{2, 2}};

int main() {
	
	solution(4,3, param);
	
	return 0;
}
