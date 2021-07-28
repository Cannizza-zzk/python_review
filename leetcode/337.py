# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.dp = {}
    def rob(self, root: TreeNode) -> int:
        if root in self.dp:
            return self.dp[root]
        if root == None:
            self.dp[root] = 0
            return 0
        
        # not rob root
        not_root = self.rob(root.left) + self.rob(root.right)

        # rob root
        rob_root = root.val
        if root.left != None and root.right != None:
            rob_root += (self.rob(root.left.left) + self.rob(root.left.right) + self.rob(root.right.left) + self.rob(root.right.right))
        elif root.left == None and root.right != None:
            rob_root += (self.rob(root.right.left) + self.rob(root.right.right))
        elif root.right == None and root.left != None:
            rob_root += (self.rob(root.left.left) + self.rob(root.left.right))
        else:
            rob_root += 0

        self.dp[root] = max(not_root,rob_root)
        return self.dp[root]
