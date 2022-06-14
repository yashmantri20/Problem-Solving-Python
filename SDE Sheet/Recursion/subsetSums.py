def helper(arr, temp, i, ans):
    if i == len(arr):
        ans.append(temp)
        return
    
    #take
    helper(arr, temp + arr[i], i + 1, ans)
    
    #not take
    helper(arr, temp, i + 1, ans)
class Solution:
	def subsetSums(self, arr, N):
		# code here
		ans = []
		helper(arr, 0, 0, ans)
		return ans