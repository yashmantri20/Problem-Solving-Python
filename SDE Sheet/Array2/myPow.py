class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x ** n
        def helper(x,n):
            if n == 0:
                return 1
            elif n % 2 == 0:
                return helper( x * x, n // 2 )
            else:
                return x * helper(x * x, (n - 1) // 2)            
        ans = helper(x,abs(n))
        if n >= 0:
            return ans
        else:
            return 1 / ans
            
        