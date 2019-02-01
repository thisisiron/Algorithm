#include <cstdio>
#include <cstring>

char str[1000001];

int main() {
	int count = 0;
	fgets(str,sizeof(str),stdin);
	if(str[0]!=' ') count++;
	for(int i=0;i<strlen(str)-1;i++){
		if(str[i]==' '&&str[i+1]!=' '&&str[i+1]!='\n')
			count++;
	}
	printf("%d", count);
	
	return 0;
}
