from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map=defaultdict(list) #add empty list into dictionary to append value easily
        ans=[] # to store values of dictionary
        for s in strs:
            sorted_s=tuple(sorted(s)) #converted in tuple because dictionary use immutable key
            my_map[sorted_s].append(s) #storing values for same sorted keys
        for value in my_map.values():
            ans.append(value) 
        return ans