class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
       
        # Initialize an empty stack to maintain the decreasing order
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_i = stack.pop()
                res[prev_i] = i - prev_i

            stack.append(i)

        return res


        