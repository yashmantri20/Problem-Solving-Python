class Solution:
    def minSteps(self, s: str, t: str) -> int:
        temp = {}
        temp1 = {}
        for i in s:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        
        for j in t:
            if j not in temp1:
                temp1[j] = 1
            else:
                temp1[j] += 1
        count = 0
        for i in temp:
            if i in temp1:
                if temp[i] > temp1[i]:
                    count += temp[i] - temp1[i]
            else:
                count += temp[i]
        return count