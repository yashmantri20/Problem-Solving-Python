class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        maxVal = 0
        if not nums:
            return 0
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                count += 1
            elif nums[i] == nums[i+1]:
                pass
            else:
                if maxVal < count:
                    maxVal = count
                count = 1
        if maxVal > count:
            return maxVal
        else:
            return count
        
        # s, longest = set(nums), 0
        # for num in s:
        #     if num - 1 in s: continue
        #     j = 1
        #     while num + j in s: j += 1
        #     if longest < j:
        #         longest = j
        # return longest

