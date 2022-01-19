class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len(list(filter(lambda x: len(str(x))%2==0 , nums)))
        