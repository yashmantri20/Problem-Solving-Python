class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        letterCount = s.count(letter)
        return (letterCount * 100) // len(s)
        