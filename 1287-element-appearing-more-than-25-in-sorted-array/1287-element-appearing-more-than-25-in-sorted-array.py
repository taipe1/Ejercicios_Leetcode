class Solution:
    def findSpecialInteger(self, A: List[int]) -> int:
        return max(set(A), key = A.count)