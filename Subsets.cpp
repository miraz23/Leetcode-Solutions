class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>>res;
        vector<int>arr;
        subset(0, nums, arr, res);

        return res;
    }

    void subset(int idx, vector<int>&nums, vector<int>&arr, vector<vector<int>>&res){
        // cout << "Index: " << idx << endl;
        if(idx == nums.size()){
            res.push_back(arr);
            return;
        }

        //pick
        arr.push_back(nums[idx]);
        subset(idx + 1, nums, arr, res);


        //unpick
        arr.pop_back();
        subset(idx + 1, nums, arr, res);


    }
};