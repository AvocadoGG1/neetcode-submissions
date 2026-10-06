class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        def helper(i, path, target):
            if target == 0:
                res.append(path.copy())
                return
            if i == len(candidates) or candidates[i] > target:
                return
            path.append(candidates[i])
            helper(i + 1, path, target - candidates[i])
            path.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i +=1 
            helper(i + 1, path, target)
        helper(0, [], target)
        return res