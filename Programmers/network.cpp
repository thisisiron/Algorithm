#include <string>
#include <vector>
#include <stack>
using namespace std;


int N;
int visited[200];
int count;
stack<int> s;

void dfs(vector<vector<int>>& computers, int start){
	s.push(start);
	while(!s.empty()){
		int i = s.top();
		s.pop();
		
		if(visited[i]==0) visited[i] = 1;
		for(int j=0;j<computers.size();j++){
			if(computers[i][j] == 1 && visited[j]==0){
				s.push(j);
			}
		}
		
	}
}


int solution(int n, vector<vector<int>> computers) {
    count = 0;
    N = n;
 	for(int i=0;i<n;i++) visited[i]=0;
 	for(int i=0;i<n;i++){
 		if(visited[i]==0){
			dfs(computers, i);
 			count++; 
		}
	}
	
    return count;
}

vector<vector<int>> param1{{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};
vector<vector<int>> param2{{1, 1, 0}, {1, 1, 1}, {0, 1, 1}};
int main() {
	
	int ans1 = solution(3, param1);
	int ans2 = solution(3, param2);
	
	printf("%d\n%d", ans1,ans2);
	return 0;
}
