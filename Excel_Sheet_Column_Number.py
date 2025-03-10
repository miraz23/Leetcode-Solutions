# Link: https://leetcode.com/problems/excel-sheet-column-number/

class Solution(object):
    def titleToNumber(self, columnTitle):
        ans = 0
        for c in map(ord, columnTitle):
            ans = ans * 26 + c - ord("A") + 1
        return ans