class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        characters = {'(': ')', '{': '}', '[': ']'}
        for i in s:
            if i in characters:
                stack.append(characters[i])
            elif len(stack) == 0 or stack.pop() != i:
                return False
        return len(stack) == 0