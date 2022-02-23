# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(L1, L2):
            s = None
            if L1.val <= L2.val:
                s , L1 = L1, L1.next
            else:
                s , L2 = L2, L2.next

            ans = s

            while L1 and L2:
                if L1.val <= L2.val:
                    s.next , L1 = L1, L1.next
                else:
                    s.next , L2 = L2, L2.next
                s = s.next

            if L1 == None:
                s.next = L2
            else:
                s.next = L1
            return ans

        if not head or not head.next:
            return head
        pre, ptr_1, ptr_2 = None, head, head
        while ptr_2 and ptr_2.next:
            pre, ptr_1 = ptr_1, ptr_1.next
            ptr_2 = ptr_2.next.next

        pre.next = None
        L1 = self.sortList(ptr_1)
        L2 = self.sortList(head)
        return merge(L1,L2)