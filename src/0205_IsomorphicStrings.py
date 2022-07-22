class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = dict()
        for idx, c in enumerate(s):
            if c not in map:
                if t[idx] not in map.values():
                    map[c] = t[idx]
                else:
                    return False
            else:
                if map[c] != t[idx]:
                    return False
        return True

    def using_match(self, s: str, t: str) -> bool:
        map = dict()
        for idx, c in enumerate(s):
            match (c in map, map.get(c, None) == t[idx], t[idx] in map.values()):
                case (False, _, False): map[c] = t[idx]
                case (False, _, True): return False
                case (True, False, _): return False
                case (True, True, _): continue

        return True


def test_is_isomorphic():
    assert Solution().isIsomorphic("egg", "add") is True
    assert Solution().isIsomorphic("foo", "bar") is False
    assert Solution().isIsomorphic("paper", "title") is True
    assert Solution().isIsomorphic("badc", "baba") is False


def test_short_but_vague():
    assert Solution().using_match("egg", "add") is True
    assert Solution().using_match("foo", "bar") is False
    assert Solution().using_match("paper", "title") is True
    assert Solution().using_match("badc", "baba") is False
