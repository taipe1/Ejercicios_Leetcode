class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans=0
        while (n>=k):
            ans+=n%k
            n//=k
        return ans +n
        