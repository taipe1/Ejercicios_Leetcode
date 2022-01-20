class Solution:
    def isValid(self, s: str) -> bool:
        pila = []
        cadena = {")":"(","]":"[","}":"{"}
        for i in s:
            if(i in cadena.values()):
                pila.append(i)
            elif((len(pila)!=0) and (cadena[i]== pila[-1])):
                pila.pop()
            else:
                return False
        return len(pila) == 0