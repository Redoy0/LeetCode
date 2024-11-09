class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        mapp={')':'(','}':'{',']':'['}
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stk.append(i) 
            else:
                if not stk:
                    return False
                else:
                    popped=stk.pop()
                    if popped!=mapp[i]:
                        return False

        
        if not stk:
            return True
        else:
            return False
