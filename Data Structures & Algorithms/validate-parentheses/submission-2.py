class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for char in s:
            #print(stack)
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                match char:
                    case ']':
                        if not stack or stack.pop() != '[':
                            return False
                    case '}':
                        if not stack or stack.pop() != '{':
                            return False
                    case ')':
                        if not stack or stack.pop() != '(':
                            return False  
        if not stack:
            return True
        return False