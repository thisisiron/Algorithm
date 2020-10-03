#include <cstdio>
#include <cstring>

using namespace std;

char str[31];
int sum[31];
int stack[31];
int top;

int main() {
	scanf("%s", &str);
	
	for(int i=0;i<strlen(str);i++){
		
		if(str[i]=='('){
			stack[top++] = 2;
		} 
		else if(str[i]=='['){
			stack[top++] = 3;
		} 
		else if(str[i]==')'){
			
			if(top==0||stack[top-1]!=2) {
				sum[0] = 0;
				break;
			}
			else {
				if(str[i-1]=='(') sum[top-1]+=2;
				else sum[top-1] += sum[top]*2;
				sum[top--] = 0;
			}
			
		} else if(str[i]==']'){
			
			if(top==0||stack[top-1]!=3){
				sum[0] = 0;
				break;
			}
			else {
				if(str[i-1]=='[') sum[top-1]+=3;
				else sum[top-1] += sum[top]*3;
				sum[top--] = 0;
			}
		}
	}
	if(top>0)sum[0]=0;
	printf("%d\n", sum[0]);
	
	return 0;
}
