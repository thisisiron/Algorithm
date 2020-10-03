#include <iostream>
#include <list> 
using namespace std;
int main() {
	int number;
	list<int> remainder;
	for(int i=0; i<10; i++){
		scanf("%d", &number);
		remainder.push_back(number % 42);
	}
	
	remainder.sort();
	remainder.unique();
	cout << remainder.size() << endl;
	
	
	
	return 0;
}
