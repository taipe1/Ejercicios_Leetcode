class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        return sum([i != j and nums[i]+nums[j] == target for i in range(len(nums)) for j in range(len(nums))])