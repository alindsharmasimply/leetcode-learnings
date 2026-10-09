import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        mid = 0

        while low < high:
            mid = low + (high - low) // 2

            total_hours = sum(math.ceil(pile / mid) for pile in piles)

            if total_hours <= h:
                high = mid
            else:
                low = mid + 1

        return low
