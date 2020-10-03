#include <cstdio>

char str[101];

int main() {
	while(fgets(str, sizeof(str), stdin))
		for(int i=0;str[i];i++)printf("%c",str[i]);
	
	
	return 0;
}
