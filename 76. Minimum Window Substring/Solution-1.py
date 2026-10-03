from collections import Counter
from math import inf


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)  # e.g., if t="ABC", count = {'A':1, 'B':1, 'C':1}
        left = 0  # The left pointer
        required = len(t)  # Total characters we need to find (e.g., 3)
        min_length = len(s) + 1  # Impossible large number instead of infinity
        best_left = -1  # Stores the starting index of our best answer

        for right, char in enumerate(s):
            count_t[char] -= 1  # Reduce the count for the character we just saw
            if count_t[char] >= 0:  # Was this character actually needed?
                required -= 1  # If yes, then we can reduce 'required' because we've got one now. We are one step closer to a valid window!
            while (
                required == 0
            ):  # The window is valid! It contains all characters of t.
                if right - left + 1 < min_length:
                    min_length = right - left + 1  # Record the new shorter length
                    best_left = left  # Record the new best starting position
                count_t[
                    s[left]
                ] += 1  # We are moving 'left' past this character, so give it back to the count
                if (
                    count_t[s[left]] > 0
                ):  # Did giving it back mean we now lack a required character?
                    required += 1  # If it goes above 0, our window is no longer valid!
                left += 1  # Move the left pointer forward

        return "" if best_left == -1 else s[best_left : best_left + min_length]
