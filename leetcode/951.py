# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flip_node(self, root):
        root.left , root.right = root.right, root.left
        return root
    
    def node_equal(self, node1 , node2):
        if node2 == None and node1 == None:
            return True
        elif node1 == None or node2 == None:
            return False
        elif node2.val == node1.val:
            return True
        else:
            return False


    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        t1_queque , t2_queue = [] , []
        #print(root1,root2)
        if root1 != None:
            t1_queque.append(root1)
        if root2 != None:
            t2_queue.append(root2)
        #print(len(t1_queque),len(t2_queue))
        while len(t2_queue) != 0 and len(t1_queque) != 0:
            node1 , node2 = t1_queque.pop(0) , t2_queue.pop(0)
            if (self.node_equal(node1,node2) and
                self.node_equal(node1.left,node2.left) and
                self.node_equal(node1.right, node2.right)):
                if node1.left != None:
                    t1_queque.append(node1.left)
                    t2_queue.append(node2.left)
                if node2.right != None:
                    t1_queque.append(node1.right)
                    t2_queue.append(node2.right)
            elif (self.node_equal(node2,node1) and
                  self.node_equal(node2.left,node1.right) and
                  self.node_equal(node1.left,node2.right)):
                self.flip_node(node1)
                if node1.left != None:
                    t1_queque.append(node1.left)
                    t2_queue.append(node2.left)
                if node2.right != None:
                    t1_queque.append(node1.right)
                    t2_queue.append(node2.right)
            else:
                return False

        if len(t2_queue) == len(t1_queque):
            return True
        else:
            return False

# BFS solution simply simulation

