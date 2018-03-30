#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the pangrams function below.
 */
string pangrams(string s) {
    /*
     * Write your code here.
     */
    int alpha[25] = {0};
    for(int i=0;i<s.size();i++){
        if(65<=s[i]&&s[i]<=90){
            alpha[s[i]-65] = 1;
        }
        else{
            alpha[s[i]-97] = 1;
        }
    }
    
    for(int j=0;j<25;j++){
        if(alpha[j]==0)
            return "not pangram";
    }
    
    return "pangram";

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = pangrams(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
