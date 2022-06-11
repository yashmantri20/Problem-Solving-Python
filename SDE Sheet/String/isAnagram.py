class Solution:
    def isAnagram(self, version1: str, version2: str) -> bool:
        temp = {}
        temp1 = {}
        for i in version1:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        for i in version2:
            if i not in temp1:
                temp1[i] = 1
            else:
                temp1[i] += 1
        return temp == temp1