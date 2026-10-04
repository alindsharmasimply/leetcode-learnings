from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        freq = defaultdict(int)
        max_fruits = 0

        left = 0
        for right, fruit in enumerate(fruits):
            freq[fruit] += 1
            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                left += 1
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
