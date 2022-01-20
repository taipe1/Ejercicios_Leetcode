class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maximum = max(nums)
        for i in range(len(nums)):
            if nums[i] == maximum:
                maxindex = i
            if nums[i] != maximum and maximum < 2*(nums[i]):
                return -1
        return maxindex
    
