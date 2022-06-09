class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] + nums[i] + nums[j] == target:
                        result.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] + nums[i] + nums[j] < target:
                        l += 1
                    else:
                        r -= 1
        return list(result)