class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0,0
        while nums:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                ss = 0 
                while ss != s:
                    s = nums[s]
                    ss = nums[ss]
                return ss
        return 0
           
        
        
    
        