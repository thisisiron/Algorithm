#include <string>
#include <vector>

using namespace std;
int D[501][501];

int max(int a, int b) {
	return (a>b) ? a:b;
}

int solution(vector<vector<int>> triangle) {
    int answer = 0;
    
    D[0][0] = triangle[0][0];
    for(int i=1;i<triangle.size();i++){
    	for(int j=0;j<triangle[i].size();j++){
    		D[i][j] = max(D[i-1][j],D[i-1][j-1]) + triangle[i][j];
		}
	}
	
	for(int i=0;i<triangle[triangle.size()-1].size();i++){
		answer = max(answer, D[triangle.size()-1][i]);
	}
    printf("%d\n", answer);
    
    return answer;
}

vector<vector<int>> param{{7}, {3, 8}, {8, 1, 0}, {2, 7, 4, 4}, {4, 5, 2, 6, 5}};

int main() {
	
	solution(param);
	
	return 0;
}
