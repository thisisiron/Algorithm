#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    int person = stages.size();
    for(int i=0;i<N;i++){
    	int mycount = count(stages.begin(), stages.end(),i+1);
//    	answer.push_back(i+1)
    	printf("%f ",(double)mycount/person );
    	person -= mycount;
	}
    
    return answer;
}

int main() {
	vector<int> st{2, 1, 2, 6, 2, 4, 3, 3};	
	solution(5,st);
	
	return 0;
}
