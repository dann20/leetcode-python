class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        comb = set()
        encoding = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        for word in words:
            repr = ""
            for c in word:
                repr += encoding[ord(c) - ord("a")]
            comb.add(repr)
        return len(comb)


def test_unique_morse_representations():
    assert Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]) == 2
    assert Solution().uniqueMorseRepresentations(["a"]) == 1
