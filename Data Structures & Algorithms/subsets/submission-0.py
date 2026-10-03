class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset,curSet = [], []
        def helper(i, nums, curSet, subset):
            if i == len(nums):
                subset.append(curSet.copy())
                return
            curSet.append(nums[i])
            helper(i + 1, nums, curSet, subset)
            curSet.pop()

            helper(i + 1, nums, curSet, subset)
        helper(0, nums, curSet, subset)
        return subset
    