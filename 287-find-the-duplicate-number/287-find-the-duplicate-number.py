class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        aux = {}
        for i in nums:
            if(i not in aux):
                aux[i]=1
            else:
                aux[i]=aux[i]+1
                
        for a,b in aux.items():
            if( b>1):
                return a
        