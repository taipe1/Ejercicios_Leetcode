class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0 or x > 2 ** 31 -1:
            return False
        return  math.floor(math.sqrt(x))
        