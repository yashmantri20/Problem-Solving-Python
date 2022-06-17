class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        temp = ''
        j = 0
        for i in words:
            temp += i
            if s[j:len(temp)] != temp:
                return False
            if s == temp:
                return True
            
        