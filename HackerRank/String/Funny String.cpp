#include <bits/stdc++.h>

using namespace std;

string funnyString(string s){
    // Complete this function
    string r = s;
    char val1, val2;
    reverse(r.begin(), r.end());
    for(int i=0;i<s.size()-1;i++){
        val1 = abs(s[i+1] - s[i]);
        val2 = abs(r[i+1] - r[i]);
        if(val1 != val2)
            return "Not Funny";
    }
    return "Funny";
}

int main() {
    int q;
    cin >> q;
    for(int a0 = 0; a0 < q; a0++){
        string s;
        cin >> s;
        string result = funnyString(s);
        cout << result << endl;
    }
    return 0;
}
