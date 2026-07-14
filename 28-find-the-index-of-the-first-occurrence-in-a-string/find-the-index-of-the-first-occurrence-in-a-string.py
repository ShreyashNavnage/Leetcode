class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_haystack = len(haystack)
        n_needle = len(needle)
        for i in range(n_haystack - n_needle + 1):
            if haystack[i:i + n_needle] == needle:
                return i
        return -1