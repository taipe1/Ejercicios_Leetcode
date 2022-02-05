class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        aux = str(bin(n))[2:]
        temp = aux[0]
        for i in range(len(aux)-1):
            if(temp != (aux[i+1])):
                temp = aux[i+1]
            else:
                return False
        return True
            
            
        