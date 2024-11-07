class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]

        for e in operations:
            if e=='D':
                stack.append(stack[-1]*2)
            elif e=='+':
                stack.append(stack[-1]+stack[-2])
            elif e=='C':
                stack.pop()
            else:
                stack.append(int(e))
        return sum(stack)