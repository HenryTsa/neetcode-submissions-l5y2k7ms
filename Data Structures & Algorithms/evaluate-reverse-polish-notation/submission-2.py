class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = [] 
        for token in tokens:
            #print(token,num_stack)
            if token.lstrip('-').isdigit():
                num_stack.append(int(token))
                #print(token,num_stack)
            else:
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                match token:
                    case '+':
                        num_stack.append(num2+num1)
                    case '-':
                        num_stack.append(num2-num1)
                    case '*':
                        num_stack.append(num2*num1)
                    case '/':
                        num_stack.append(int(num2/num1))
        #print(token,num_stack[-1])
        return num_stack[-1]