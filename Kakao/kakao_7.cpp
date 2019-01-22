#include <string>
#include <vector>

using namespace std;



void check() {
    for(int i=0;i<board.size()-1;i++){
        for(int j=0;j<board.size();j++){
            if(board[i][j]!=0) {

            }
        }
    }
}


int solution(vector<vector<int>> board) {
    int answer = 0;

    

    for(int i=0;i<board.size()-1;i++){
        for(int j=0;j<board.size();j++){
            if(board[i-1][j-1] == 0 && i>0 && j>0){
                if(j > 0 && board[i][j]!=0 && board[i+1][j-1]==board[i][j]) {
                    board[i][j-1] = board[i][j];
                } else if(j<board[0].size()-1 && board[i][j]!=0 && board[i+1][j+1]==board[i][j] && board[i+1][j+1]==0) {
                    board[i][j+1] = board[i][j];
                }
            }
        }
    }
    

    for(int i=0;i<board.size();i++) {
        for(int j=0;j<board[0].size();j++) {
            printf("%d ", board[i][j]);
        }
        printf("\n");
    }



    return answer;
}





vector<vector<int>> b{{0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,4,0,0,0},{0,0,0,0,0,4,4,0,0,0},{0,0,0,0,3,0,4,0,0,0},{0,0,0,2,3,0,0,0,5,5},{1,2,2,2,3,3,0,0,0,5},{1,1,1,0,0,0,0,0,0,5}};
int main() {
    solution(b);
    return 0;
}