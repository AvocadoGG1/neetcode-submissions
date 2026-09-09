# Definition for singly-linked lists.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        k = len(lists)
        interval = 1
        while interval < k:
            for i in range(0, k - interval, interval *2):
                lists[i] = self.mergeTwo(
                    lists[i], lists[i + interval]
                )
            interval *= 2
        return lists[0]
    def mergeTwo(self, l1, l2) -> Optional[ListNode]:
        if not l1:
            return l2
        elif not l2:
            return l1
        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        return dummy.next