class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #Pascal Triangle
        finalAns = [[1] * i for i in range(1, numRows + 1)]
        for i in range(2,numRows):
            for j in range(1, i):
                finalAns[i][j] = finalAns[i-1][j - 1] + finalAns[i-1][j]
        return finalAns