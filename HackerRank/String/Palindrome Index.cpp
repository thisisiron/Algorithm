#include <bits/stdc++.h>

using namespace std;

bool isPalindrome(string s){
    int i=0;
    int j= s.size()-1;
    while(i<j){
        if(s[i]!=s[j]) return false;
        i++;
        j--;
    }
    return true;
    
}


int palindromeIndex(string s){
    // Complete this function
    int idx = -1;
    int i=0,j=s.size()-1;
    while(i<j && s[i]==s[j]){ 
        i++;
        j--;
    }
    
    if(i<j){
        string str1 = s.substr(0,i) + s.substr(i+1,s.size()-i+1);
        if(isPalindrome(str1)) idx = i;
        string str2 = s.substr(0,j) + s.substr(j+1,s.size()-j+1);
        if(isPalindrome(str2)) idx = j;
    }
    
    
    return idx;
}

int main() {
    int q;
    cin >> q;
    for(int a0 = 0; a0 < q; a0++){
        string s;
        cin >> s;
        int result = palindromeIndex(s);
        cout << result << endl;
    }
    return 0;
}
