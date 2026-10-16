class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse=True)

        for pos, spd in cars:
            time_to_reach_target = (target - pos) / spd
            if not stack or time_to_reach_target > stack[-1]:
                stack.append(time_to_reach_target)

        return len(stack)
