#include <cstdio>
#include <vector>
using namespace std;

struct info{
	int node, cost;
};

int N;
int M;
vector<info> network[1001];

int main() {
	scanf("%d", &N);
	scanf("%d", &M);
	
	for(int i=1;i<=M;i++){
		int a,b,cost;
		scanf("%d %d %d",&a,&b,&cost);
		network[a].push_back({b,cost});
	}
	
	
	
	return 0;
}
