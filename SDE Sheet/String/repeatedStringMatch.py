class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        temp = a
        count = 1
        while len(temp) < len(b) :
            temp += a
            count += 1
        if b in temp:
            return count
        temp += a
        count += 1
        if b in temp:
            return count
        return -1