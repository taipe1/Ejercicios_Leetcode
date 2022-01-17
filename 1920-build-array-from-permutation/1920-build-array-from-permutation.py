class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        aux = []
        for i in range(len(nums)):
            aux.append(nums[nums[i]])
        return aux
        