class Solution:
    def reverseWords(self, s: str) -> str:
        s=" "+s
        n=len(s)-1
        l=0
        r=0
        temp=""
        ans=""
        flag=True
        for i in range(n,-1,-1):
            if s[i]!=" ":
                temp+=s[i]
            else:
                if temp!="":
                    if flag:
                        ans+=temp[::-1]
                        flag=False
                    else:
                        ans+=" "+temp[::-1]
                    temp=""
        return ans




            #"a good   example"
