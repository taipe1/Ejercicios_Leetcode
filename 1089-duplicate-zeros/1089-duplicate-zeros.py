class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        j = 0
        while(j<len(arr)):
            if(arr[j] == 0):
                arr.pop()
                arr.insert(j,0)
                j=j+1
            j=j+1
        return arr

        