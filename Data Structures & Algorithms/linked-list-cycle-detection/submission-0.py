# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        visitedNodes = set()
        
        cur = head
        while cur:
        
            if cur in visitedNodes:
                return True
            else: 
                visitedNodes.add(cur)
            cur = cur.next
               
        return False