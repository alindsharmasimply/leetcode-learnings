from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(len(prefix)):
            for item in strs[1:]:
                if (len(prefix) <= len(item) and prefix != item[: len(prefix)]) or len(
                    prefix
                ) > len(item):
                    prefix = prefix[:-1]
        return prefix
