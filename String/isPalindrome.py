class Solution:
    def isPalindrome(self, x: int) -> bool:
        # temp, rev = 0, 0
        # val = x
        # x = abs(x)
        # while x != 0:
        #     temp = x % 10
        #     rev = rev * 10 + temp
        #     x = x // 10
        # return val == rev
        if x < 0:
            return False
        temp = str(x)[::-1]
        return temp == str(x)