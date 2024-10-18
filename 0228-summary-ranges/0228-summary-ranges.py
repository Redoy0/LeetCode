class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return nums
        start=0
        end=0
        ans=[]
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                end=i+1
            else:
                if start==end:
                    ans.append(f'{nums[start]}')
                    start=i+1
                    end=start
                else:
                    ans.append(f'{nums[start]}->{nums[end]}')
                    start=end+1
                    end=start
        if nums[len(nums)-1]-nums[end-1]==1:
            ans.append(f'{nums[start]}->{nums[end]}')
        else:
            ans.append(f'{nums[start]}')
        return ans

