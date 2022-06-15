class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def helper(temp, i):
            if i == len(nums):
                if temp not in finalAns:
                    finalAns.append(temp[:])
                return

            #take
            temp.append(nums[i])
            helper(temp, i + 1)

            #not take
            temp.pop()
            helper(temp, i + 1)
        finalAns = []
        helper([], 0)
        return finalAns