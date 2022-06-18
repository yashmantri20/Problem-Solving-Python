class Solution:
    def findLucky(self, arr: List[int]) -> int:
        temp = {}
        for i in arr:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        ans = -1
        for i in temp:
            if i == temp[i] and ans < i:
                ans = i
        return ans
        