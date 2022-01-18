class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        valor1 = int(str(num)[::-1])
        valor2 = int(str(valor1)[::-1])
        return num == valor2
        