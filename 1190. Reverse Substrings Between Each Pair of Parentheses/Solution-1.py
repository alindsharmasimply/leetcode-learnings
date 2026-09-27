class Solution:
    def reverseParentheses(self, s: str) -> str:
        # brute force
        stack = []
        ans = []
        for char in s:
            if char == '(':
                stack.append(len(ans))
            elif char == ')':
                i = stack.pop()
                ans[i:] = ans[i:][::-1]
            else:
                ans.append(char)
        
        return ''.join(ans)