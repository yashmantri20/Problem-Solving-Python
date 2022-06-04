def helper(n, newDict) -> int:
    sum = 0
    temp = n
    while n > 0:
        sum += (n % 10) ** 2
        n = n // 10

    if temp not in newDict:
        newDict[temp] = sum
            
    if sum == 1:
        return True
    
    if sum in newDict:
        return False
    return helper(sum, newDict)

class Solution:            
    def isHappy(self, n: int) -> bool:        
        newDict = {}
        return helper(n, newDict)