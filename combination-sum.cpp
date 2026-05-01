class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>>res;
        vector<int>arr;
        comsum(0, target, candidates, arr, res);

        return res;
    }

    void comsum(int idx, int target, vector<int>&candidates, vector<int>&arr, vector<vector<int>>&res){
        if(target < 0 || idx == candidates.size()) return;
        
        if(target == 0){
            res.push_back(arr);
            return;
        }


        arr.push_back(candidates[idx]);
        comsum(idx, target - candidates[idx], candidates, arr, res);

        arr.pop_back();
        comsum(idx + 1, target, candidates, arr, res);
    }
};