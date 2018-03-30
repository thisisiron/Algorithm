#include <bits/stdc++.h>

using namespace std;

string twoStrings(string s1, string s2){
    // Complete this function
    for(int i=0;i<s1.size();i++){
        if(s2.find(s1[i])!=-1)
            return "YES";
    }
    return "NO";
}

int main() {
    int q;
    cin >> q;
    for(int a0 = 0; a0 < q; a0++){
        string s1;
        cin >> s1;
        string s2;
        cin >> s2;
        string result = twoStrings(s1, s2);
        cout << result << endl;
    }
    return 0;
}
