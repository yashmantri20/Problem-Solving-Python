class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        for i in strs:
            k = tuple(sorted(i))
            temp[k] = temp.get(k, []) + [i]
        return temp.values()
        
        