#include <iostream>
#include <deque>
using namespace std;

int main(){
	int N, M;
	int temp, idx;
	int count = 0;
	
	
	scanf("%d %d", &N, &M);
	deque<int> d;
	for(int k=1;k<=N;k++)
		d.push_back(k);
	for(int i=0;i<d.size();i++){
		cout<<d[i]<< " ";
	}
	for(int j = 0; j < M; j++){
		scanf("%d", &idx);
		if(idx==d.front()){
			d.front();
			d.pop_front();
			continue;
		} else if(idx == d.back()){
			d.back();
			d.pop_back();
			continue;
		}
		if(N/2>=idx){
			for(deque<int>::size_type i=0; i <idx-1 ; i++){
				temp = d.front();
				d.pop_front();
				d.push_back(temp);
				count++;
				if(idx == d.front()){
					d.front();
					d.pop_front();
					break;
				}
			}
		} else {
			for(deque<int>::size_type i=d.size(); i > idx ; i--){
				temp = d.back();	
				d.pop_back();
				d.push_front(temp);
				count++;
				if(idx == d.back()){
					d.back();
					d.pop_back();
					break;
				}
			}
		}

	}
	for(int i=0;i<d.size();i++){
		cout<<d[i]<< " ";
	}
	cout << endl;
	printf("%d", count);

	
	
	return 0;
}
