class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # ans = []
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[j]<nums[i]:
        #             count+=1
        #     ans.append(count)
        # return ans
        dic = {}
        ans=[]
        sorted_nums=sorted(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in dic:
                dic[sorted_nums[i]]=i
        
        for i in nums:
            ans.append(dic[i])
        return ans