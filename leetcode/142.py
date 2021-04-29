# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        node_dict = {}
        index = 0
        while True:
            if head == None:
                return None
            
            if node_dict.get(head) == None:
                node_dict[head] = index
                index += 1
                head = head.next
            else:
                return head


        