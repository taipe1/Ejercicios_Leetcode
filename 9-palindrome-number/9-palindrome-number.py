class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x > 2 **31 - 1:
            return False
        return str(x) == str(x)[::-1]