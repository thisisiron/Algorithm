#include <string>
#include <vector>

using namespace std;

int answer = -1;

void dfs(int N, int idx, int current, int target){
	if(idx>8) return;	
	if(current==target) {
		if(idx < answer || answer == -1) {
			answer = idx;
		}
		return;
	}
	int nn = 0;
	for(int i=0;i<8;i++){
		nn = nn * 10 + N;
		dfs(N, idx+1+i, current + nn, target);
		dfs(N, idx+1+i, current - nn, target);
		dfs(N, idx+1+i, current * nn, target);
		dfs(N, idx+1+i, current / nn, target);
	}
	
}


int solution(int N, int number) {
    answer = -1;
    
    dfs(N, 0, 0, number);
    
    printf("%d\n", answer);
    
    return answer;
}


int main() {
	
	solution(5,12);
	solution(2,11);
	
	
	return 0;
}
