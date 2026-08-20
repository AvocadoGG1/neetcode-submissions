class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque()
        l = 0
        res = []
        maxCur = 0 
        for r in range(len(nums)):
            slidingWindow = r - l + 1
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if q[0] < l:
                q.popleft()
            if slidingWindow == k:
                
                res.append(nums[q[0]])
                l += 1
           
        return res