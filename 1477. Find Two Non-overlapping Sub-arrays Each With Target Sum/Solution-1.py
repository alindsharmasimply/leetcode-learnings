from math import inf


class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        prefix_sum = 0
        left = 0
        dp = [inf] * n
        result = inf

        for right in range(n):
            prefix_sum += arr[right]

            while prefix_sum > target:
                prefix_sum -= arr[left]
                left += 1

            dp[right] = dp[right - 1] if right - 1 >= 0 else inf

            if prefix_sum == target:
                current_length = right - left + 1
                result = min(
                    result, current_length + dp[left - 1] if left - 1 >= 0 else inf
                )
                dp[right] = min(dp[right], current_length)

        return result if result != inf else -1
