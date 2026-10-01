class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0
        left = 0

        for right, char in enumerate(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(char)
            max_length = max(max_length, right - left + 1)

        return max_length
