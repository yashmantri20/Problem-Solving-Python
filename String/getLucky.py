class Solution:
    def getLucky(self, s: str, k: int) -> int:
        temp = ''
        for i in s:
            temp += str(ord(i) - ord('a') + 1)
        i = 0
        while i < k:
            val = 0
            for j in temp:
                val += int(j)
            temp = str(val)
            i += 1
        return temp
        