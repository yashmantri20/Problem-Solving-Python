class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        temp = []
        temp1 = []
        for i in nums:
            if i > 0:
                temp.append(i)
            else:
                temp1.append(i)
        ans = []
        for i in range(len(temp)):
            ans.append(temp[i])
            ans.append(temp1[i])
        return ans
                
                
            