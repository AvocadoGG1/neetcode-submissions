class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        num = 0
        for i in tokens:
            if i not in "-+*/":
                stack.append(int(i))
            if i in "-+*/" and len(stack) >= 2:
                element1 = stack.pop()
                element2 = stack.pop()
                if i == "+":
                    result = element2 + element1
                elif i == "-":
                    result = element2 - element1
                elif i == "*":
                    result = element2 * element1
                elif i == "/":
                    result = int(element2 / element1)
                stack.append(result)
                result = 0
        num = stack.pop()
        return int(num)