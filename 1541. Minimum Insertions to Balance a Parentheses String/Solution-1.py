class Solution:
    def minInsertions(self, s: str) -> int:
        needed_right = 0  # Increment by 2 for each '('
        missing_left = 0  # Increment by 1 for each missing '('
        missing_right = 0  # Increment by 1 for each missing ')'

        for char in s:
            if char == "(":
                if needed_right % 2 == 1:
                    missing_right += 1
                    needed_right -= 1
                needed_right += 2
            else:
                needed_right -= 1
                if needed_right < 0:
                    missing_left += 1
                    needed_right += 2

        return needed_right + missing_left + missing_right
