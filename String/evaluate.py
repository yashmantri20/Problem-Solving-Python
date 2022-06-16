class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {k: v for k, v in knowledge}
        res = []
        cur = ''
        going = False
        for c in s:
            if c == '(':
                going = True
            elif c == ')':
                going = False
                res.append(d.get(cur, '?'))
                cur = ''
            elif going:
                cur += c
            else:
                res.append(c)
        return ''.join(res)
        # temp = ''
        # ans = ''
        # d = {k:v for k, v in knowledge}
        # for c in s:
        #     if c == '(':
        #         ans += temp
        #         temp = ''
        #     elif c == ')':
        #         if temp in d:
        #             ans += d[temp]
        #             temp = ''
        #         if temp:
        #             ans += '?'
        #             temp = ''
        #     else:
        #         temp += c
        # if temp:
        #     ans += temp
        # return ans
                
        