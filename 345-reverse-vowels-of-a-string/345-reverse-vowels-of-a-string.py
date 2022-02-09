class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        red = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        left = 0
        right = len(s) - 1
        while(left < right):
            if(s[left] not in red):
                left += 1
                continue
            if(s[right] not in red):
                right -= 1
                continue
            else:
                s[left],s[right] = s[right],s[left]
                right -= 1
                left += 1
        return (''.join(s))
            