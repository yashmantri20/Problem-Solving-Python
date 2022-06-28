class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for i in words:
            strLen = len(i)
            if i == s[:strLen]:
                count += 1
        return count
        