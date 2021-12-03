# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # tree = left_son + root + right_son
        # a FBT's left and right son should be FBT or sigle node

        res = []
        if n == 1:
            return [TreeNode()]

        for i in range(1,n-1,2):
            
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n-1-i)
            
            for left_child in left:
                for right_child in right:
                    root = TreeNode()
                    root.left = left_child
                    root.right = right_child
                    #print(root)
                    res += [root]
        
        return res