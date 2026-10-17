from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(num: int):
            summ = 0
            while num != 0:
                d = num % 10
                summ += d
                num //= 10
            return summ

        sorted_pairs = sorted((get_digit_sum(x), x) for x in nums)

        target_index_map = {
            value: index for index, (_, value) in enumerate(sorted_pairs)
        }

        n = len(nums)

        visited = [False] * n

        min_swaps = 0

        for i in range(n):
            if visited[i] or target_index_map[nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = target_index_map[nums[j]]
                cycle_size += 1

            if cycle_size > 0:
                min_swaps += cycle_size - 1

        return min_swaps
