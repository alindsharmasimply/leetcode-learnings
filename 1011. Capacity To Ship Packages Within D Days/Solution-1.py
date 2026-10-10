class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def can_ship(capacity: int) -> bool:
            current_days = 1
            current_load = 0
            for w in weights:
                if current_load + w > capacity:
                    current_days += 1
                    current_load = w
                else:
                    current_load += w
            return current_days <= days

        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2
            if can_ship(mid):
                high = mid - 1  # Try a smaller capacity
            else:
                low = mid + 1  # Need a larger capacity

        return low
