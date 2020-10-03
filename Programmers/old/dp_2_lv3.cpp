#include <string>
#include <vector>

using namespace std;

long long solution(int N) {
    long long answer = 0;
    long long a = 1;
    long long b = 1;
    long long c = 0;
    for(int i=0;i<N-1;i++){
    	c = a + b;
    	a = b;
    	b = c;
	}
	
	answer = a*2 + c*2;
	
    return answer;
}


int main() {
	
	solution(5);
	solution(6);
	
	return 0;
}
