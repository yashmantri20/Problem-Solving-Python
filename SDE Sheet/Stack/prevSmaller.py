class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
          res = [-1] * len(A)
          stack = []

          for i in range(len(A)-1, -1, -1):
              while stack and A[i] < A[stack[-1]]:
                  res[stack.pop()] = A[i]
              stack.append(i)
              
          return res