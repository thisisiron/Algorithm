#include <cstdio>
#include <vector>
#include <queue>
#define INF 20000 * 10
using namespace std;

struct info{
	int node;
	int weight;
	info(int v, int w){
		node = v;
		weight = w;
	}
	bool operator < (const info &ref) const {
		return weight > ref.weight;
	}
};
int V,E;
int start;
int D[20001] = {INF};
priority_queue<info> pq;
vector<info> adj[20001];

int main() {
	scanf("%d %d", &V, &E);
	scanf("%d", &start);
	
	int u,v,w;
	
	for(int i=1;i<=V;i++){
		D[i] = INF;
	}
	
	for(int i=1;i<=E;i++){
		scanf("%d %d %d", &u,&v,&w);
		adj[u].push_back(info(v,w));
	}
	
	D[start] = 0;
	pq.push({start,0});
	while(!pq.empty()){
		info temp = pq.top();
		pq.pop();
		
		int node = temp.node;
		int weight = temp.weight;
		
		if(D[node]!=weight) continue;
		
		for(info next:adj[node]){
			if(D[next.node]>D[node] + next.weight){
				D[next.node] = D[node] + next.weight;
				pq.push(info(next.node, D[next.node]));
			}
		}
		
	}
	
	for(int i=1;i<=V;i++){
		if(D[i]==INF){
			printf("INF\n");
			continue;
		}
		printf("%d\n",D[i]);
	}
	
	return 0;
}
