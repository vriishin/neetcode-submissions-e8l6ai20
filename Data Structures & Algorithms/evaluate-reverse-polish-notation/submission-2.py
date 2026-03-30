class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numstac = []
        
        for c in tokens: 
            if c == '+':
                b = numstac.pop()
                a = numstac.pop()
                numstac.append(a + b)
            elif c == '-':
                b = numstac.pop()
                a = numstac.pop()
                numstac.append(a - b)
            elif c == '*':
                b = numstac.pop()
                a = numstac.pop()
                numstac.append(a * b)
            elif c == '/':
                b = numstac.pop()
                a = numstac.pop()
                numstac.append(int(a / b))  # truncates toward 0
            else:
                numstac.append(int(c))
        
        return numstac[0]
