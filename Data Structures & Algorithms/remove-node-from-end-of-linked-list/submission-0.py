# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, cur = None, head
        count = 0 
        while cur:
            count += 1
            cur = cur.next 
        position = count - n
        cur = head
        index = 0
        while cur:
            if position == 0:
                return head.next
            if index == position:
                prev.next = cur.next
                break
            else:   
                index += 1 
                prev = cur
                cur = cur.next
        return head