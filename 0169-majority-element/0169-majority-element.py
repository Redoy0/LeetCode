class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result=-1
        counter=0
        for num in nums:
            if counter == 0:
                result=num
            if num==result:
                counter+=1
            elif num!=result:
                counter-=1
        return result