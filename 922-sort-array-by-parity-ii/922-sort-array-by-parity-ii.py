class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        aux = [None]*len(nums)
        par = 0
        impar = 1
        for i in nums:
            if(i%2 == 0):
                aux[par] = i
                par += 2
            else:
                aux[impar] = i
                impar += 2
        return aux