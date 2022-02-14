class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        cadena = ''.join(i if i.isdigit() else ' ' for i in word).split()
        return (len(set(list(map(int, cadena)))))
            
        