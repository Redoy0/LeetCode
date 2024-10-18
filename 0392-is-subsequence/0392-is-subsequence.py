class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls=len(s)
        lt=len(t)
        if ls>lt: return False
        if s=="": return True
        j=0
        for i in range(lt):
            if t[i]==s[j]:
                if j==ls-1:
                    return True
                j+=1
        return False
        