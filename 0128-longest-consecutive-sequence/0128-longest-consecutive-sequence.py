class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums=list(set(nums))
        nums.sort()
        Len=[]
        currLen=1

        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                currLen+=1
            else:
                Len.append(currLen)
                currLen=1
        Len.append(currLen)
        return max(Len)