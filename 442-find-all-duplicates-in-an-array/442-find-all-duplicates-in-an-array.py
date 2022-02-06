class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        nums.clear()
        return list([i for i in count if count[i] > 1])
