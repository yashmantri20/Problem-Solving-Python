class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        temp = []
        j = 0
        for i in pushed:
            temp.append(i)
            while temp and temp[-1] == popped[j]:
                temp.pop()
                j += 1
        return len(temp) == 0
        