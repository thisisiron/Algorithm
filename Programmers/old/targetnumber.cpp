#include <string>
#include <vector>

using namespace std;

int N;
int count;

void dfs(vector<int> numbers, int target, int sum, int k){
	if(k == N) {
		if(target == sum){
			count++;
			printf("%d\n", count);
		}
		return;
	} 
	else {
		sum += numbers[k];
		dfs(numbers, target, sum, k+1);
		sum -= numbers[k];
		sum -= numbers[k];
		dfs(numbers, target, sum, k+1);
	}
}

int solution(vector<int> numbers, int target) {
    N = numbers.size();
    dfs(numbers, target, 0, 0);
    return count;
}


vector<int> param{1, 1, 1, 1, 1};
int main() {
	solution(param, 3);
	
	return 0;
}
