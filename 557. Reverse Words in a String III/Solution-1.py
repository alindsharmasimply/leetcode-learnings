class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(word: str):
            return "".join(reversed(word))

        s_list = s.split(" ")
        final_s = ""
        for item in s_list:
            final_s += reverse(item) + " "

        return final_s.strip()
