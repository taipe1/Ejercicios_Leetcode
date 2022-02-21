class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mayor = len(nums)/2
        dicc = {}
        for i in nums:
            if i in dicc:
                dicc[i]=dicc[i] + 1
            else:
                dicc[i]=1
        for ele,val in dicc.items():
            if(val > mayor):
                return ele
        
            
        