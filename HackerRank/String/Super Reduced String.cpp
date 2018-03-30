#include <bits/stdc++.h>

using namespace std;

string super_reduced_string(string s){
    // Complete this function
    L:
        for(int i=0; i<s.size()-1;i++){
            if(s.empty()){
                s = "Empty String";
                break;
            }
            if(s[i]==s[i+1]){
                s.erase(i, 2);
                goto L;
            }
        }

    
    return s;
}

int main() {
    string s;
    cin >> s;
    string result = super_reduced_string(s);
    cout << result << endl;
    return 0;
}

