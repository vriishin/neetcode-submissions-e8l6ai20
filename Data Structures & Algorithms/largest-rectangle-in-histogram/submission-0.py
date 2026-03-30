class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =[]
        maxA = 0

        for i, h in enumerate(heights):
            startingIndex = i 
            while stack and h<=stack[-1][1]:
                A = (i - stack[-1][0]) * (stack[-1][1])
                maxA = max(A,maxA)
                stackI, stackH = stack.pop()
                startingIndex = stackI

            stack.append((startingIndex, h))
        
        for i, h in stack:
            A = (len(heights)- i) * ( h)
            maxA = max(maxA, A)
        return maxA
