class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        newstr=""
        if len(word1)>=len(word2):
            for i in range(len(word2)):
                newstr+=word1[i]
                newstr+=word2[i]
            newstr+=word1[len(word2):]
        elif len(word1)<len(word2):
            for i in range(len(word1)):
                newstr+=word1[i]
                newstr+=word2[i]
            newstr+=word2[len(word1):]
        return newstr
        

        
            
        