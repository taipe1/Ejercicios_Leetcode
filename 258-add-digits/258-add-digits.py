class Solution:
    def addDigits(self, num: int) -> int:
        if(num %9 == 0 and num != 0):
            return 9
        else:
            return (num)%9
        