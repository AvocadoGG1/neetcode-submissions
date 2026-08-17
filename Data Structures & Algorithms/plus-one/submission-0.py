class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        res = []

        for digit in digits:
            num = num * 10 + digit
        num += 1 
        while num > 0:
            curdigit = num % 10 
            res.append(curdigit)
            num = num // 10
        res.reverse()
        return res