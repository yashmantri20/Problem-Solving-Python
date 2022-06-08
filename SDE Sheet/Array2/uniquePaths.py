class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #DP
        table = [[0 for x in range(n)] for x in range(m)]
        for i in range(m):
            table[i][0] = 1
        for i in range(n):
            table[0][i] = 1
        for i in range(1,m):
            for j in range(1,n):
                table[i][j] = table[i-1][j] + table[i][j-1]
        return table[m-1][n-1]
        #Recursion
        # def helper(left, right):
        #     if left >= m:
        #         return 0
            
        #     if right >= n:
        #         return 0
            
        #     if left == m - 1 and right == n - 1:
        #         return 1
        #     else:
        #         return helper(left + 1, right) + helper(left, right + 1)
        
        # return helper(0,0)