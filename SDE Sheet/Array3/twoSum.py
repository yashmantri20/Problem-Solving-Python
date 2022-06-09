class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        # i = 0
        # j = 0
        # for x in range(len(nums)):
        #     a = target - nums[x]
        #     if a in nums[x + 1:]:
        #         i = x
        #         j = a
        #         break
        # for y in range(i + 1, len(nums)):
        #     if nums[y] == j:
        #         j = y
        #         break
        # return [i,j]
        
        temp = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in temp:
                return [temp[t], i]
            else:
                temp[nums[i]] = i