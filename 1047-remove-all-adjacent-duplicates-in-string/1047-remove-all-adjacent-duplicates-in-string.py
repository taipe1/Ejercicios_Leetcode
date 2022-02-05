class Solution:
    def removeDuplicates(self, s: str) -> str:
        pila = []
        for i in s:
            if( pila and i == pila[-1]):
                pila.pop()
            else:
                pila.append(i)
        return ''.join(pila)
        