class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {} # Maps a character to its most recent index
        left = 0      # Left pointer of our sliding window
        max_length = 0
        
        for right, char in enumerate(s):
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            char_map[char] = right
            max_length = max(max_length, right - left + 1)
            
        return max_length