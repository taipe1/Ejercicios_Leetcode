class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suma = (n*(n+1))//2
        actual_suma = sum(nums)
        diferencia = sum(set(nums))
        return [actual_suma - diferencia  ,suma - diferencia]
        