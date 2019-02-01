#include <cstdio>

char chess[8][9];

int main() {
	int count = 0;
	for(int i=0;i<8;i++)
		for(int j=0;j<9;j++)
			scanf("%c",&chess[i][j]);
	
	for(int i=0;i<8;i++){
		for(int j=0;j<9;j++){
			
			if(i%2==0&&j%2==0){
				if(chess[i][j]=='F') count++;
			}
			else if(i%2==1&&j%2==1){
				if(chess[i][j]=='F') count++;
			}

					
		}
	}
	
	printf("%d", count);
	return 0;
}
