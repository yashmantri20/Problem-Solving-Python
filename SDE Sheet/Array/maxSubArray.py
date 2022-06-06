class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane Algo
        maxTotal = nums[0]
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            if temp > maxTotal:
                maxTotal = temp
                
            if temp < 0:
                temp = 0
        return maxTotal