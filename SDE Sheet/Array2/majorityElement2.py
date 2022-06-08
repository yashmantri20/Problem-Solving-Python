class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        temp = {}
        ans = []
        for i in nums:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
            if temp[i] > len(nums) / 3 and i not in ans:
                ans.append(i)
        return ans