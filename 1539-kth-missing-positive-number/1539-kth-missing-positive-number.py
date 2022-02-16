class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr)
        while(l < r):
            m = ( l + r ) // 2
            if arr[m] - 1 - m < k:
                l = m+1
            else:
                r = m
        return (l+k)
        
            
        