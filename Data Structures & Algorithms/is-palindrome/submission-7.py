class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s) - 1
        for l, lv in enumerate(s):
            if l > r:
                break
            if lv.isalnum():
                while not s[r].isalnum():
                    r -= 1
                if lv.lower() != s[r].lower():
                    return False
                r -= 1
        return True
