class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        lista = list(str(n))
        prod = 1
        for i in lista:
            prod = prod * int(i)
            
        lista1 = list(str(n))
        suma = 0
        for i in lista1:
            suma = suma +  int(i)
        return prod - suma
    
    
    

                

        