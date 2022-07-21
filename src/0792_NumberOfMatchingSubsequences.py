class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        from collections import defaultdict

        waiting = defaultdict(list)
        for it in map(iter, words):
            waiting[next(it)].append(it)

        for c in s:
            for it in waiting.pop(c, []):
                waiting[next(it, None)].append(it)

        return len(waiting[None])

    def slow_and_dumb(self, s: str, words: list[str]) -> int:
        s = list(s)
        count = 0

        for word in words:
            word = list(word)
            count += 1
            prev_idx = -1
            for c in word:
                if c in s[prev_idx + 1:]:
                    prev_idx = s.index(c, prev_idx + 1)
                elif c not in s[prev_idx + 1:]:
                    count -= 1
                    break

        return count


def test_num_matching_subseq():
    assert Solution().numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]) == 3
    assert Solution().numMatchingSubseq("dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]) == 2
    assert Solution().numMatchingSubseq("abc", ["a", "bb", "acd", "ace"]) == 1
    assert Solution().numMatchingSubseq("abc", ["a", "bb", "acd", "ace", "abc"]) == 2
    assert Solution().numMatchingSubseq("abc", ["a", "b", "c"]) == 3
