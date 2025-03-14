# Link: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        current = head
        
        while current and current.next:
            gcd_val = math.gcd(current.val, current.next.val)
            new_node = ListNode(gcd_val)

            new_node.next = current.next
            current.next = new_node
            
            current = new_node.next
        
        return head