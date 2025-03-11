# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

class Solution(object):
    def inorderTraversal(self, root):
        result = []
        self.helper(root, result)
        return result

    def helper(self, node, result):
        if node:
            self.helper(node.left, result)
            result.append(node.val)
            self.helper(node.right, result)