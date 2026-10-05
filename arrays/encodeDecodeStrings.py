class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += len(s) + "#" + s
        return encoded

    def decode(self, encoded: str) -> List[str]:
        res = []
        i = 0

        while i < len(encoded):
            j = i
            while encoded[j] != "#":
                j += 1
            # breaks at #
            wordLength = int(encoded[i:j])
            word = encoded[j + 1 : j + 1 + wordLength]
            res.append(word)
            i = j + 1 + wordLength

        return res
