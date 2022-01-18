class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        suma = nums[0]
        aux = nums[0]
        for i in range(1,len(nums)):
            if(nums[i] > nums[i-1]):
                suma += nums[i]
            else:
                suma = nums[i]
            aux = max(aux,suma)
        return aux
        