# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Please implement encode and decode

# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        return "".join(str(len(s)) + "/" + s for s in strs)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, s):
        i = 0
        decoded = []
        while i < len(s):
            slash = s.find("/", i)
            length_of_word = int(s[i:slash])
            i = slash + length_of_word + 1
            decoded.append(s[slash + 1 : i])
        return decoded
