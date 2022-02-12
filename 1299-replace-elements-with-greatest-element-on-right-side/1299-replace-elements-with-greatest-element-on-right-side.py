class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        aux = []
        for i in range(len(arr)-1):
            aux.append(max(arr[i+1:]))
        aux.append(-1)
        return aux
        