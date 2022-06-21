class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = str(int("".join(map(str,digits))) + 1)
        ans = []
        for i in temp:
            ans.append(i)
        return ans