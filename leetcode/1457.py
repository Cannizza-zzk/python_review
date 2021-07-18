# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.path = {}
        self.cnt = 0

    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
       
        def is_leaf(node):
            if node.left == None and node.right == None:
                return True
            return False
        
        def dfs(node):
            # current node
            if node.val in self.path:
                self.path[node.val] += 1
            else:
                self.path[node.val] = 1
            # next step
            if is_leaf(node):
                odd_cnt = 0
                for index ,val in self.path.items():
                    if val % 2 == 1:
                        odd_cnt += 1
                    if odd_cnt == 2:
                        break
                self.cnt = self.cnt + 1 if odd_cnt < 2 else self.cnt
            else:
                if node.left != None:
                    dfs(node.left)
                if node.right != None:
                    dfs(node.right)
            
            # recover
            if self.path[node.val] == 1:
                del self.path[node.val]
            else:
                self.path[node.val] -= 1
            return

        dfs(root)
        return self.cnt


                

