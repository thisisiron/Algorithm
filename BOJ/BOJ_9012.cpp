#include <cstdio>
#include <stack>

using namespace std;


int T;
char input[51];

int main() {
	
	scanf("%d", &T);
	
	while(T--){
		stack<int> s;
		int i;
		scanf(" %s", input);
		if(input[0]=='\n'){
			printf("NO\n");	
		}
		for(i=0;input[i];i++){

			if(input[i]=='(') {
				s.push(1);
			}	
			
			if(input[i]==')') {
				if(s.empty()) {
					printf("NO\n");
					break;
				}
				else if(s.top()==1) {
					s.pop();
				}
			}
		}
		if(s.empty()&&!input[i]){
			printf("YES\n");	
		} 
		else if(!s.empty()&&!input[i]) {
			printf("NO\n");	
		}
		
	}
	
	
	
	return 0;
}
