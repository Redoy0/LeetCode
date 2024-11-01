from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        my_map=defaultdict(int)
        for t in text:
            if t in "balloon":
                my_map[t]+=1
        if len(my_map) !=5:
            return 0
        else:
            return min(my_map['b'],my_map['a'],my_map['l']//2,my_map['o']//2,my_map['n'])

