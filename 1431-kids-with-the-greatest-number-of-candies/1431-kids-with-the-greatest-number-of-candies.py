class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        may = max(candies)
        arr = [False] * len(candies)
        for i in range(len(candies)):
            if((candies[i] + extraCandies) >= may):
                arr[i]=True

        return arr
        

        