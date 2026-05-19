class Solution:
    def isValid(self, s: str) -> bool:
        # U: string with brackets, return the string if each bracket has a partner, closed in correct order 
        # s = [] true, s = ([{}]) true, s = [(]) not correct order

        # M: Stack and a queue
        # P: Initiate a stack, append a bracket, if the same bracket appears then we go through the stack and pop. If the stack is emptpy then its valid. 
        stack = []
        if len(s) == 0:
            return True
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for i in s:
            if i in "{[(":
                stack.append(i)
            if i in "})]":
                if stack and stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False