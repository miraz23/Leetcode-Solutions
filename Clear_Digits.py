class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for i in range(len(s)):
            if s[i].isdigit() and result:
                result.pop()
            else:
                result.append(s[i])

        return "".join(result)
        
        