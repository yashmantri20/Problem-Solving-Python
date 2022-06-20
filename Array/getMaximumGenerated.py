class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        temp = [0, 1]
        for i in range(1, n//2 + 1):
            if 2 * i <= n:
                temp.append(temp[i])
            if 2 * i + 1 <= n:
                temp.append(temp[i] + temp[i+1])
        return max(temp)
        