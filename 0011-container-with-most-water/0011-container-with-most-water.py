class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA=0
        l=0
        n=len(height)
        r=n-1
        while l<r:
            if height[l]<=height[r]:
                w=r-l
                A=w*height[l]
                maxA=max(maxA,A)
                l+=1
            else:
                w=r-l
                A=w*height[r]
                maxA=max(maxA,A)
                r-=1

        return maxA



            