class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    def pop(self) -> None:
        if len(self.stack) == 0:
            return "Stack is empty"
        
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return "Stack is empty"
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
