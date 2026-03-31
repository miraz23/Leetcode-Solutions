class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>>mp;
        for(string s: strs){
            string x = s;
            sort(s.begin(), s.end());
            mp[s].push_back(x);
        }
        vector<vector<string>>res;
        for(const auto &p : mp){
            res.push_back(p.second);
        }
        return res;
    }
};