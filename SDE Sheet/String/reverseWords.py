class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split(' ')
        temp = []
        for i in a:
            if i != '':
                temp.append(i)
        return ' '.join(temp[::-1]) 

        # temp = []
        # word = ''
        # for i in s:
        #     if i != ' ':
        #         word += i
        #     elif len(word) > 0:
        #         temp.append(word)
        #         word = ''
        # if(len(word) > 0):
        #     temp.append(word)
        # return ' '.join(temp[::-1])