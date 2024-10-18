class Solution(object):
    def findClosestNumber(self, nums):
        mini=nums[0]
        for i in nums:
            if abs(i)<abs(mini):
                mini=i
        if mini<0 and abs(mini) in nums:
            return abs(mini)
        else:
            return mini


        