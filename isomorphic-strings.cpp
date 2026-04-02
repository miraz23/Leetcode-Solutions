class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char>mpS, mpT;
        int l = s.size();
        for(int i = 0; i < l; i++){
            mpS[s[i]] = t[i];
            mpT[t[i]] = s[i];
        }

        for(int i = 0; i < l; i++){
            if(mpS[s[i]] != t[i] || mpT[t[i]] != s[i])
            return false;
        }

        return true;
    }
};