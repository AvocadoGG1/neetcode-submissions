class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Subsets method
        res = []
        def helper(i, cur, total):
            if i >= len(nums):
                return
            if total == target:
                res.append(cur.copy())
                return
            if total > target:
                return 
           
            cur.append(nums[i])
            helper(i, cur, total + nums[i])
            cur.pop()
            helper(i + 1, cur, total)
        helper(0, [], 0)
        return res