#include <cstdio>

int R;
char str[21];

int main() {
	int T;
	
	scanf("%d", &T);
	
	while(T--) {
		scanf("%d %s", &R, &str);

		for(int i=0; str[i];i++) {
			for(int j=0; j<R; j++) {
				printf("%c", str[i]);
			}
		}
		printf("\n");
	}
	
	return 0;
}
