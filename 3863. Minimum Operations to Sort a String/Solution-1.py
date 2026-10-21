class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # The string is already sorted
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0

        # The string is not sorted and has only two elements hence it's impossible to sort
        if n == 2:
            return -1

        min_global_ASCII_index = 0
        max_global_ASCII_index = 0

        for i in range(n):
            if s[i] < s[min_global_ASCII_index]:
                min_global_ASCII_index = i
            if s[i] >= s[max_global_ASCII_index]:
                max_global_ASCII_index = 0

        # In this case, either one of the boundaries is sorted hence the remaining one can be sorted in just one sort action
        if min_global_ASCII_index == 0 or max_global_ASCII_index == n - 1:
            return 1

        # This is the worst-case scenario when the entire string is kind of in descending order. Example: "cba"
        if max_global_ASCII_index == 0 and min_global_ASCII_index == n - 1:
            return 3

        # The standard case where only two operations are sufficient
        return 2
