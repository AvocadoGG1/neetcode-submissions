class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        def helper(i):
            if i == len(nums):
                res.append(path.copy())
                return

            # take it
            path.append(nums[i])
            helper(i+1)
            path.pop()

            # skip it (and all its copies)
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper(i+1)

        helper(0)
        return res