class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_index = {c: i for i, c in enumerate(s)}
        stack = []
        visited = set()
        for i, char in enumerate(s):
            if char in visited:
                continue

            while stack and stack[-1] > char and last_index[stack[-1]] > i:
                visited.remove(stack.pop())

            visited.add(char)
            stack.append(char)

        return "".join(stack)
