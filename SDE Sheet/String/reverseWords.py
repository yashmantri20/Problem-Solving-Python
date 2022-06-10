class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split(' ')
        temp = []
        for i in a:
            if i != '':
                temp.append(i)
        return ' '.join(temp[::-1]) 