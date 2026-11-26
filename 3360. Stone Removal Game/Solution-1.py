class Solution:
    def canAliceWin(self, n: int) -> bool:
        current_count = 10
        alice_turn = True
        while n >= 0:
            n = n - current_count
            alice_turn = not alice_turn
            current_count -= 1
        return alice_turn