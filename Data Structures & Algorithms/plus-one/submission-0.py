class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nu = digits[-1] + 1
        carry = nu // 10
        out = [nu % 10]
        for digit in reversed(digits[:-1]):
            nu = carry + digit
            out.insert(0, nu % 10)
            carry = nu // 10
        if carry:
            out.insert(0, carry)
        return out