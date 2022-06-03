class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zeroPos = 0
        
        for i in range(n):
            if nums[i] != 0:
                nums[zeroPos],nums[i] = nums[i],nums[zeroPos]
                zeroPos +=1