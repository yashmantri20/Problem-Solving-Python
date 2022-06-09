class Solution:
    def maxLen(self, n, arr):
        #Code here
        temp = {}
        total = 0
        maxVal = 0
        for i in range(len(arr)):
            total += arr[i]
            
            if total is 0:
                maxVal = i + 1
            
            if total not in temp:
                temp[total] = i
            else:
                maxVal = max(maxVal, i - temp[total])
        return maxVal
        