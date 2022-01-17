class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        minimos = []
        for i in range(len(nums)):
            if(i%10 == nums[i]):
                minimos.append(i)
        if(len(minimos) < 1):
            return -1
        return min(minimos)
        