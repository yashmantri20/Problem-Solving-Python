class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lengthOfNeedle = len(needle)
        for i in range(len(haystack)):
            s = haystack[i:lengthOfNeedle + i]
            if s == needle:
                return i
        return -1