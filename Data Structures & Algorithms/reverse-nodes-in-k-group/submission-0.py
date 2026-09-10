# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        check = head

        for _ in range(k):
            if check is None:
                return head
            check = check.next
        def reverse(cur, prev, counter):
            if cur is None or counter == k:
                return prev, cur
            else:
                nextNode = cur.next
                cur.next = prev
                counter += 1
                return reverse(nextNode, cur, counter)

        newHead, nextGroup = reverse(head, None, 0)

        head.next = self.reverseKGroup(nextGroup, k)

        return newHead

        
