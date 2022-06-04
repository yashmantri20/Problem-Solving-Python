class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        while i < len(nums):
            if nums[i] % 2 != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 2
            else:
                i += 2
        return nums