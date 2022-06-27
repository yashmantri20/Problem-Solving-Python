class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # temp = {}
        # for i in nums:
        #     if i not in temp:
        #         temp[i] = 1
        #     else:
        #         temp[i] += 1
        # for i in temp:
        #     if temp[i] == 1:
        #         return i
        return 2*sum(set(nums)) - sum(nums)
        