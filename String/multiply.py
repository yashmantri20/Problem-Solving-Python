def helper(num):
    temp = 0
    for i in num:
        temp = temp * 10 + ord(i) - ord('0')
    return temp

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        str1 = helper(num1)
        str2 = helper(num2)
        return str(str1 * str2)