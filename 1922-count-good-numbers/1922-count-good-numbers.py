class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD=int(10**9+7)

        fives,fours=n//2+n%2,n//2
        return (pow(5,fives,MOD) * pow(4,fours,MOD)) % MOD
        