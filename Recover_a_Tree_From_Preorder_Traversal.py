# Link: https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

class Solution(object):
    def recoverFromPreorder(self, traversal):
        stack = []
        i = 0

        while i < len(traversal):
            depth = 0
            while i < len(traversal) and traversal[i] == '-':
                depth += 1
                i += 1

            start = i

            while i < len(traversal) and traversal[i].isdigit():
                i += 1
            
            val = int(traversal[start:i])
            node = TreeNode(val)

            while len(stack) > depth:
                stack.pop()

            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

            stack.append(node)

        return stack[0]