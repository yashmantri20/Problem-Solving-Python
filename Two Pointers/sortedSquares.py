class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # ans = []
        # for i in nums:
        #     ans.append(i * i)
        # ans.sort()
        # return ans
        start, end = 0, len(nums) - 1
        ans = [None for i in nums]
        writeIndex = len(nums) - 1
        while start <= end:
            if abs(nums[start]) > abs(nums[end]):
                ans[writeIndex] = nums[start] ** 2
                start += 1
            else:
                ans[writeIndex] = nums[end] ** 2
                end -= 1
            writeIndex -= 1
        return ans
            