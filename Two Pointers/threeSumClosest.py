class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        result = float('inf')
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                a = nums[l] + nums[r] + nums[i]
                if a > target: r -= 1
                elif a < target: l += 1
                else: return a
                if abs(target - a) < abs(target - result):
                    result = a
        return result