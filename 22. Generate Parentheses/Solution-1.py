class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(
            opened_parenthesis: int, closed_parenthesis: int, combination: str
        ):

            if opened_parenthesis == closed_parenthesis == n:
                result.append(combination)

            if opened_parenthesis < n:
                backtrack(opened_parenthesis + 1, closed_parenthesis, combination + "(")

            if closed_parenthesis < opened_parenthesis:
                backtrack(opened_parenthesis, closed_parenthesis + 1, combination + ")")

        backtrack(0, 0, "")
        return result
