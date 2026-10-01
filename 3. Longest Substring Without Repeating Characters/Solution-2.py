from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen_index = defaultdict(int)
        max_length = 0
        left = 0

        for right, char in enumerate(s):
            if s[right] in last_seen_index and last_seen_index[s[right]] >= left:
                left = last_seen_index[s[right]] + 1
            last_seen_index[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length
