class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]

        for i in tokens:
            if i in "+-*/":
                r=int(stk.pop())
                l=int(stk.pop())
                if i=='+':
                    stk.append(l+r)
                elif i=='-':
                    stk.append(l-r)
                
                elif i=='*':
                    stk.append(l*r)
                
                elif i=='/':
                    stk.append(l/r)
            else:
                stk.append(i)
        return int(stk[0])           

