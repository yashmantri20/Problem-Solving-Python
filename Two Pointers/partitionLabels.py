class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        i = 0
        strLen = s.rindex(s[0])
        ans = []
        prevLen = 0
        for i in range(len(s) - 1):
            if strLen == i:
                ans.append(strLen + 1 - prevLen)
                prevLen = strLen + 1
            if s.rindex(s[i+1]) > strLen:
                strLen = s.rindex(s[i+1])
        if prevLen != len(s):
            ans.append(strLen + 1 - prevLen)
        return ans
        
        