class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_map={}
        for i in nums:
            if i in my_map and my_map[i]>=1:
                return True

            my_map[i]=my_map.get(i,0)+1
        return False
        