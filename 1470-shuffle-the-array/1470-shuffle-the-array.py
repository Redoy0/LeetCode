class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        myA=[]
        for i in range(n):
           myA.append(nums[i])
           myA.append(nums[i+n]) 

        return myA