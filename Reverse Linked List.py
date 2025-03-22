# Link: https://leetcode.com/problems/reverse-linked-list/

class Solution(object):
    def reverseList(self, head):
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev