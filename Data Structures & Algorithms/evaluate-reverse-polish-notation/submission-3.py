class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = int(tokens[0]) if tokens else 0

        for i in range(len(tokens)):
            if tokens[i] not in ['+', '-', '*', '/']:
                stack.append(int(tokens[i]))

            if tokens[i]=='+':
                total+= int(stack.pop())
            if tokens[i]=='-':
                total-=int(stack.pop())
            if tokens[i]=='*':
                total = total * int(stack.pop())
            if tokens[i]=='/':
                total = total / int(stack.pop())

        return total 
                    