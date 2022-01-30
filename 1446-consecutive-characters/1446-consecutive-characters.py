class Solution:
    def maxPower(self, s: str) -> int:
        mayor = 1
        aux = s[0]
        cont = 1
        for i in s[1:]:
            if (aux == i):
                cont = cont + 1
            else:
                mayor = max(cont,mayor)
                cont=1
                aux = i
        return max(cont,mayor)
        