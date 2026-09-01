# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head
        
        # Use slow and fast pointers, slow is middle
        while f and f.next:
            s = s.next
            f = f.next.next
        # reverse
        prev, cur = None, s
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        first = head
        second = prev

        while second.next:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
    
