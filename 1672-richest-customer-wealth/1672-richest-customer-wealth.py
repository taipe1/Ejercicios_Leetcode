class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        s = 0
        aux = -9999
        for i in accounts:
            s = 0
            for j in i:
                s = s + j 
            if(s > aux):
                aux = s 
        return aux
                
        