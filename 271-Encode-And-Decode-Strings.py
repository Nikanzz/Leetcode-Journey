class Solution:

    def encode(self, strs: List[str]) -> str:
        combined = ""
        for string in strs:
            combined += str(len(string)) + "_" + string
        return combined

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "_":
                j += 1
            length = int(s[i:j])
            ret.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return ret
