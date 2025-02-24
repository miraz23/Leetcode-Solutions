# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
    
        ans = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] not in ans:
                ans.append(nums[i])
        
        nums[:len(ans)] = ans
        return len(ans)