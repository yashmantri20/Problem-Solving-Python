class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        arr = [0 for i in range(len(A))]
        for i in range(len(A)):
            if arr[A[i] - 1] == 0:
                arr[A[i] - 1] = 1
            else:
                arr[A[i] - 1] += 1
        repeatedNumber = 0
        notAppeared = 0
        for i in range(len(arr)):
            if arr[i] > 1:
                repeatedNumber = i + 1
            if arr[i] == 0:
                notAppeared = i + 1
        return [repeatedNumber,notAppeared]