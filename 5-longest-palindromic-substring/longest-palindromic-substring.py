class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
            
        def expand_around_center(left: int, right: int) -> tuple:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - left - 1
            
        start = 0
        max_length = 0
        
        for i in range(len(s)):
            start1, len1 = expand_around_center(i, i)
            start2, len2 = expand_around_center(i, i + 1)
            if len1 > max_length:
                start = start1
                max_length = len1
            if len2 > max_length:
                start = start2
                max_length = len2
        return s[start:start + max_length]