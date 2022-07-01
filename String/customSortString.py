class Solution:
    def customSortString(self, order: str, s: str) -> str:
        temp = {}
        for i in s:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        ans = ''        
        for i in order:
            if i in temp:
                ans += temp[i] * i
                del temp[i]
                
        for i in temp:
            ans += temp[i] * i
        return ans

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = ""
        for ch in order:
            for _ in range(s.count(ch)):
                ans += ch
        for ch in s:
            if ch not in order:
                ans += ch
        return ans