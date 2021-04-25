# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        evenNode = []
        if head == None:
            return head
        pnode = head
        pnext = pnode.next
        cnt = 2
        while pnext != None:
            if cnt % 2 == 0:
                evenNode.append(pnext)
                pnode.next = pnext.next
                pnext = pnext.next
            else:
                pnode = pnode.next
                pnext = pnext.next
            cnt +=  1

        pnode.next = evenNode[0] if evenNode != [] else None

        for i in range(0, len(evenNode)):
            evenNode[i].next = evenNode[i+1] if i+1 < len(evenNode) else None
             
        return head
        








# misunderstanding the meaning of the question
""" class Solution:
    def is_even(self, current_node:ListNode):
        return current_node.val % 2 == 0

    def oddEvenList(self, head: ListNode) -> ListNode:
        evenNode = []
        pnode = head
        
        while pnode != None and self.is_even(pnode):
            evenNode.append(pnode)
            pnode = pnode.next

        if pnode == None:
            head = evenNode[0]
        else:
            head = pnode
            pnext = pnode.next
            while pnext != None:
                if self.is_even(pnext):
                    evenNode.append(pnext)
                    pnode.next = pnext.next
                    pnext = pnext.next
                else:
                    pnode = pnode.next
                    pnext = pnext.next
            pnode.next = evenNode[0] if evenNode != [] else None

            for i in range(0, len(evenNode)):
                evenNode[i].next = evenNode[i+1] if i+1 < len(evenNode) else None
            
            return head """

        

