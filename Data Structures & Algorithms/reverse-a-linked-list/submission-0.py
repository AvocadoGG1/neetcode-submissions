# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head  # Start at the head node
        res = []
        while current:
            res.append(current.val)
            current = current.next  # Move to the next node
        cur = dummy = ListNode(0)
        res.reverse()
        for e in res:
            cur.next = ListNode(e)
            cur = cur.next
        
        return dummy.next
        