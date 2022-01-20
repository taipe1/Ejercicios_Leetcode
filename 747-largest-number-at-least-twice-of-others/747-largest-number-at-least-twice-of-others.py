class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        aux = max(nums)
        for i in range(len(nums)):
            if nums[i] == aux:
                retornar = i
            if nums[i] != aux and aux < 2*(nums[i]):
                return -1
        return retornar
    
