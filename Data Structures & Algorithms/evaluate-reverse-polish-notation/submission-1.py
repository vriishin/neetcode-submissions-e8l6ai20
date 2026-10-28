class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numstac = []
        op = {'+', '-','*','/'}
        total = int(tokens[0])
        for c in tokens[1:]: 
            if c == '+':
                    total += int(numstac.pop())
            elif c == '-':
                    total -= int(numstac.pop())
            elif c == '*':
                    total *= int(numstac.pop())
            elif c == '/':
                    total = int(total/float(numstac.pop()))
            else:
                numstac.append(c)
        return total


