class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        cadena = []
        i = len(s) - 1
        while (i >= 0):
            cadena.append(s[i])
            if  spaces and i == spaces[-1]:
                cadena.append(' ')
                spaces.pop()
            i = i - 1
        return (''.join(cadena)[::-1])
            