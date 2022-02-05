class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        def prime(num):
            if(num == 1):
                return False
            if(num == 2):
                return True
            else:
                for i in range(2,num):
                    if(num%i == 0):
                        return False
                    else:
                        continue
                return True
                
        cont = 0
        bandera= False
        for i in range(left,right+1):
            aux = int(str(bin(i)[2:]).count('1'))
            if(prime(aux)):
                cont = cont + 1
        return cont
            
                
                
        