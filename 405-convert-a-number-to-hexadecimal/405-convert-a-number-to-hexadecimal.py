class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        aux = '0123456789abcdef'
        cade = ''
        for i in range(8):
            cade =aux[num % 16] + cade
            num = num >> 4
        return cade.lstrip('0')