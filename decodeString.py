class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            a = ''
            num = ''
            if i != ']':
                stack.append(i)
            if i == ']':
                while stack and stack[-1] != '[':
                    a += stack.pop()[::-1]
                stack.pop()
                while stack and stack[-1].isdigit():
                    num += stack.pop()
                stack.append(int(num[::-1])*a[::-1])
        return ''.join(stack)

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():     # curNum*10+int(c) is helpful in keep track of more than 1 digit number
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString