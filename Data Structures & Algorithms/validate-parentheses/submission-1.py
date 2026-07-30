class Solution:
    def isValid(self, s: str) -> bool:
        return self.validParens(s)

    def validParens(self, s: str) -> bool:
        pairs = {']': '[', ')': '(', '}': '{'}
        stack = []
        for c in s:
            if c in pairs.values():
                stack.append(c)
            elif len(stack) == 0 or stack[-1] != pairs.get(c, None):
                return False
            else:
                stack.pop()
        return len(stack) == 0
