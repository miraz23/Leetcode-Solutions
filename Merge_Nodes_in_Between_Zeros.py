# Link: https://leetcode.com/problems/merge-nodes-in-between-zeros/

class Solution(object):
    def mergeNodes(self, head):
        dummy = ListNode()
        new_node = dummy
        current = head.next
        # print(head.next)
        sum = 0

        while current:
            if current.val == 0:
                if sum > 0:
                    new_node.next = ListNode(sum)
                    new_node = new_node.next
                sum = 0
            else:
                sum += current.val

            current = current.next

        return dummy.next