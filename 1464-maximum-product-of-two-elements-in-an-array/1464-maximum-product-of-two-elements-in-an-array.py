class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        aux = sorted(nums)[len(nums)-2:]
        return "{0}".format((aux[0]-1)*(aux[1]-1))
        