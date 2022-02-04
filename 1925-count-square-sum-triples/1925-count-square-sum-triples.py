class Solution:
    def countTriples(self, n: int) -> int:
        cont = 0
        for i in range(1,n):
            for j in range(i+1,n):
                c = math.sqrt(i**2 + j**2)
                if(c.is_integer() and c <= n):
                    cont += 2
        return cont