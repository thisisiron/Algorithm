#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct info {
	int x,y,idx;
	int left, right;
};
struct info trees[10001];
int N;

bool sortpoint(const vector<int>& v1, const vector<int>& v2){
	return (v1[1] == v2[1]) ? (v1[0] < v2[0]) : (v1[1] > v2[1]) ;
}


vector<vector<int>> solution(vector<vector<int>> nodeinfo) {
    vector<vector<int>> answer;
    sort(nodeinfo.begin(), nodeinfo.end(), sortpoint);
    N = nodeinfo.size();
    for(int i=0;i<N;i++){
    	printf("%d %d\n", nodeinfo[i][0], nodeinfo[i][1]);
	}
    
    
    for(int i=0;i<N;i++){
    	trees[i+1].x = nodeinfo[i][0];
    	trees[i+1].y = nodeinfo[i][1];
    	trees[i+1].idx = i+1;
	}
	
	for(int i=1;i<=)
	
	
    
    return answer;
}

vector<vector<int>> param{{5,3},{11,5},{13,3},{3,5},{6,1},{1,3},{8,6},{7,2},{2,2}};
int main() {
	solution(param);
	
	
	return 0;
}
