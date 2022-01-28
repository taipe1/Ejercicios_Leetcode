class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_pre = ""
        if not strs:
            return longest_pre
        shortest_str = min(strs, key=len)
        for i in range(len(shortest_str)):
            if all([x.startswith(shortest_str[:i+1]) for x in strs]):
                longest_pre = shortest_str[:i+1]
            else:
                break
        return longest_pre
        