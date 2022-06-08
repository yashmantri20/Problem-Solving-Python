class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = {}
        for i in nums:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
            if temp[i] > len(nums) / 2:
                return i
            
        # candidate, count = nums[0], 0
        # for num in nums:
        #     if num == candidate:
        #         count += 1
        #     elif count == 0:
        #         candidate, count = num, 1
        #     else:
        #         count -= 1
        # return candidate
        