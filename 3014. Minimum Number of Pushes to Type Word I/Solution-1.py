import collections


class Solution:
    def minimumPushes(self, word: str) -> int:
        freq_dict = collections.Counter(word)
        all_freqs = sorted(freq_dict.values(), reverse=True)
        return sum(((i // 8) + 1) * freq for i, freq in enumerate(all_freqs))
