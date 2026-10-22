from math import inf


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        ans = float(inf)

        is_dec = is_inc = True

        index_of_zero = nums.index(0)

        for i in range(n):
            if nums[(index_of_zero + i) % n] != i:
                is_inc = False
                break

        for i in range(n):
            if nums[(index_of_zero - i) % n] != i:
                is_dec = False
                break

        if is_inc:
            ans = min(ans, index_of_zero)
            ans = min(ans, 2 + n - index_of_zero)

        if is_dec:
            ans = min(ans, (index_of_zero + 1) % n + 1)
            ans = min(ans, n - index_of_zero)

        return ans if ans != float("inf") else -1
