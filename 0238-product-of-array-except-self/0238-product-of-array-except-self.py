class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l_mul=1
        r_mul=1

        n=len(nums)
        l_arr=[0]*n
        r_arr=[0]*n

        for i in range(n):
            j= -i -1
            l_arr[i]=l_mul
            r_arr[j]=r_mul
            l_mul*=nums[i]
            r_mul*=nums[j]

        return [l*k for l,k in zip(l_arr,r_arr)]
