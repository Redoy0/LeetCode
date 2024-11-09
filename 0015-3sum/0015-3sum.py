class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            if nums[i]>0: break
            elif i>0 and nums[i]==nums[i-1]: continue
            lo=i+1
            hi=len(nums)-1
            while lo<hi:
                
                if nums[i]+nums[lo]+nums[hi]==0:
                    ans.append([nums[i],nums[lo],nums[hi]])
                    lo,hi=lo+1,hi-1
                    while lo<hi and nums[lo] ==nums[lo-1]:
                        lo+=1
                    
                    while lo<hi and nums[hi] ==nums[hi+1]:
                        hi-=1
                    
                elif nums[i]+nums[lo]+nums[hi]<0:
                    lo+=1
                else:
                    hi-=1
        return ans