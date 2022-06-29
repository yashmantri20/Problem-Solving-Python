from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # res = []
        # for r in matrix:
        #     res += r
        # return sorted(res)[k-1]
        a, res = [], -1
        for i in matrix:
            for j in i:
                heappush(a, j)

        for _ in range(k):
            res = heappop(a)    
        return res