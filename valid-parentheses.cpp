class Solution {
public:
    bool isValid(string s) {
        stack<char>st;
        unordered_map<char, char>mp;
        mp[')'] = '(';
        mp['}'] = '{';
        mp[']'] = '[';

        for(auto& bracket: s){
            if(!mp.count(bracket)){
                st.push(bracket);
            }
            else if(!st.empty() && st.top() == mp[bracket]){
                st.pop();
            }
            else{
                return false;
            }
        }
        return st.empty();
    }
};