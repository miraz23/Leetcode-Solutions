class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if s1 == s2:
            return True

        diff = []
    
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append((s1[i], s2[i]))
        
        if len(diff) > 2:
            return False
        
        return len(diff) == 2 and diff[0] == diff[1][::-1]