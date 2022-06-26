class Solution:
    def findMedianSortedArrays(self, L: List[int], R: List[int]) -> float:
        length1 = len(L)
        length2 = len(R)
        arr = [0 for i in range(length1 + length2)]
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        length = len(arr)
        mid = length // 2
        
        if length % 2 != 0:
            median = arr[mid]
        else:
            median = (arr[mid - 1] + arr[mid]) / 2
        return median
        