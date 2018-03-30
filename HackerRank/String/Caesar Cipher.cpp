#include <bits/stdc++.h>

using namespace std;

void encode(char &ch){
    if(ch=='z'||ch=='Z')
        ch = ch-25;
    else
        ch = ch+1;
}


string caesarCipher(string s, int k) {
    // Complete this function
    for(int i=0; i<s.size(); i++){
        if(isalpha(s[i])){
            for(int j=0;j<k;j++){
                encode(s[i]);
            }
        }
    }
    
    return s;
}

int main() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    int k;
    cin >> k;
    string result = caesarCipher(s, k);
    cout << result << endl;
    return 0;
}
