#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<int> food_times, long long k) {
    int answer = 0;
    int s = food_times.size();
    map<int, int> m;
    for(int i=0;i<s;i++){
        m[food_times[i]] = i;
    }

    for(int i=0;i<s;i++) {
        printf("%d ", m.find(food_times[i])->second);
    }

    for(int i=0;i<k;i++){
        
        if(food_times[i%s]!=0)
            food_times[i%s]-=1;
        // else 
        // for(int i=0;i<food_times.size();i++) printf("%d ", food_times[i]);
    }


    // printf("\n");
    // for(int i=0;i<food_times.size();i++) printf("%d ", food_times[i]);

    return answer;
}


vector<int> a{3, 1, 2};

int main() {

    solution(a,5);

    return 0;
}