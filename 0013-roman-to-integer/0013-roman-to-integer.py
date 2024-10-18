class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        r={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)-1):
            if r[s[i]]<r[s[i+1]]:
                sum-=r[s[i]]
            else:
                sum+=r[s[i]]
        return sum+r[s[-1]]



        
            
                