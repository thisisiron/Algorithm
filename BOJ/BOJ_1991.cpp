#include <cstdio>

int N;
char str[10];
struct Node{
	int left, right, me;
};
struct Node node[26];

void preorder(int n){
	printf("%c", node[n].me);
	if(node[n].left != NULL) preorder(node[n].left);
	if(node[n].right != NULL) preorder(node[n].right);
}

void inorder(int n) {
	if(node[n].left != NULL) inorder(node[n].left);
	printf("%c", node[n].me);
	if(node[n].right != NULL) inorder(node[n].right);
}

void postorder(int n) {
	if(node[n].left != NULL) postorder(node[n].left);
	if(node[n].right != NULL) postorder(node[n].right);
	printf("%c", node[n].me);
}

int main() {
	scanf("%d ", &N);
	
	for(int i=0;i<26;i++) {
        node[i].me = i+'A';
        node[i].left = node[i].right = NULL;
    }
    
    char a,b,c;
    
	for(int i=0;i<N;i++){
		
		fgets(str,sizeof(str),stdin);
		a = str[0];
		b = str[2];
		c = str[4];
		
		if(b!='.')
			node[a-'A'].left = b - 'A';
		if(c!='.')
			node[a-'A'].right = c - 'A';
	}
	
	preorder(0);
	printf("\n");

	inorder(0);
	printf("\n");
	
	postorder(0);
	printf("\n");
	
	return 0;
}
