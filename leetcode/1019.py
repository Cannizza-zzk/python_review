# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        idx = 0
        stack, res = [], [] 
        while head:
            res.append(0)
            if len(stack) != 0:
                while len(stack) != 0 and head.val > stack[-1][0]:
                    _ , node_idx = stack.pop()
                    res[node_idx] = head.val

            stack.append([head.val, idx])
            head = head.next
            idx += 1

        return res
                
