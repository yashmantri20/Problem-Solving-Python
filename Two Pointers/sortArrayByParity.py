class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        oddVal = []
        evenVal = []
        for i in nums:
            if i % 2 == 0:
                evenVal.append(i)
            else:
                oddVal.append(i)
        return evenVal + oddVal
        