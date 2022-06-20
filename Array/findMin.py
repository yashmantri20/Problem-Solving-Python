class Solution:
    def findMin(self, num: List[int]) -> int:
        start, end = 0, len(num) - 1
        while start < end:
            mid = (start + end) // 2
            if num[mid] > num[end]:
                start = mid + 1
            else:
                end = mid
        return num[start]