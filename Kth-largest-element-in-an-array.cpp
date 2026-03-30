class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int n = 20000;
        vector<int>cnt(n+1, 0);
        for(int i = 0; i < nums.size(); i++){
            cnt[nums[i] + 10000]++;
        }

        for(int i = n; i >= 0; i--){
            k -= cnt[i];
            if(k <= 0) 
                return i - 10000;
        }

        return 0;
    }
};