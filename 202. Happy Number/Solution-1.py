class Solution:
    def isHappy(self, n: int) -> bool:
        def squared_sum(n: int) -> int:
            summ = 0
            while n != 0:
                last_digit = n % 10
                summ += last_digit**2
                n //= 10
            return summ

        slow = squared_sum(n)
        fast = squared_sum(squared_sum(n))
        while slow != fast:
            slow = squared_sum(slow)
            fast = squared_sum(squared_sum(fast))

        return slow == 1
