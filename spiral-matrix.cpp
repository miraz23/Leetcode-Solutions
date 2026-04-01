class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int row = matrix.size();
        int col = matrix[0].size();

        int top = 0;
        int right = col - 1;
        int bottom = row - 1;
        int left = 0;

        vector<int>res;

        while(left <= right && top <= bottom){
            for(int i = left; i <= right; i++){
                res.push_back(matrix[top][i]);
            }
            top++;
            for(int i = top; i <= bottom; i++){
                res.push_back(matrix[i][right]);
            }
            right--;

            if( !(left <= right && top <= bottom) ) break;
            
            for(int i = right; i >= left; i--){
                res.push_back(matrix[bottom][i]);
            }
            bottom--;
            for(int i = bottom; i >= top; i--){
                res.push_back(matrix[i][left]);
            }
            left++;
        }

        return res;
    }
};