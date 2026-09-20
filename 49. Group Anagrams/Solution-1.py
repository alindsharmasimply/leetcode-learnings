from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        word_freq = defaultdict(list)
        for word in strs:
            char_count = [0] * 26
            for character in word:
                char_count[ord(character) - 97] += 1
            key = tuple(char_count)
            word_freq[key].append(word)
        return list(word_freq.values())
