# Link: https://leetcode.com/problems/merge-two-sorted-lists/

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 is None or list2 is None:
            return list1 or list2
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2