class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        teleport = {}

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                teleport[i] = j
                teleport[j] = i


        direction = 1
        n = len(s)
        ans = []
        current_index = 0
        while current_index < n:
            if s[current_index] in '()':
                current_index = teleport[current_index]
                direction = -direction
            else:
                ans.append(s[current_index])
            current_index += direction
        
        return ''.join(ans)