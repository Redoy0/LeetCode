class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stk=[]
        ans=[0]*n
        for i,t in enumerate(temperatures):
            while stk and stk[-1][0]<t:
                temp,indx=stk.pop()
                ans[indx]=i-indx
            stk.append((t,i))
        return ans
