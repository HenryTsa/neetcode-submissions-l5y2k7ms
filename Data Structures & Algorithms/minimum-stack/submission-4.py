class MinStack:

    def __init__(self):
        self.stack = []
        self.stack2 = []
    def push(self, val: int) -> None:
        
        self.stack.append(val)
        if self.stack2:
            self.stack2.append(min(self.stack2[-1],val))
        else:
            self.stack2.append(val)
        #print(self.stack2)
    def pop(self) -> None:
        #print(self.stack)
        self.stack2.pop()
        return self.stack.pop()

    def top(self) -> int:
       # print(self.stack)
        return self.stack[-1]

    def getMin(self) -> int:
        #print(self.stack)
        return self.stack2[-1]