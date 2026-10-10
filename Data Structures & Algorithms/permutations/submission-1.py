class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        booleanArr = [False] * length
        def helper(path):
            if len(path) == length:
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if booleanArr[i]:      # step 1: the only if
                    continue           # skip used numbers
                booleanArr[i] = True    # ...mark...
                path.append(nums[i])    # ...append...
                helper( path)    # ...recurse...
                path.remove(nums[i]) # ...undo both...
                booleanArr[i] = False
        helper([])
        return res