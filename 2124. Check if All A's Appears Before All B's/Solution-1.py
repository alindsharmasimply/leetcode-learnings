class Solution:
    def checkString(self, s: str) -> bool:
        last_a = s.rfind("a")
        first_b = s.find("b")
        return first_b > last_a if last_a != -1 and first_b != -1 else True
