class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval:interval[0])
        marged=[]

        for interval in intervals:
            if len(marged)==0 or marged[-1][1]<interval[0]:
                marged.append(interval)
            else:
                marged[-1]=[marged[-1][0],max(marged[-1][1],interval[1])]
        
        return marged
    
    
    
