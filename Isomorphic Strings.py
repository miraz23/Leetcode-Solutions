# Link: https://leetcode.com/problems/isomorphic-strings/

class Solution(object):
    def isIsomorphic(self, s, t):
        st = {}
        ts = {}

        for c1, c2 in zip(s, t):
            if (c1 in st and st[c1] != c2) or (c2 in ts and ts[c2] != c1):
                return False
                
            st[c1] = c2
            ts[c2] = c1

        return True