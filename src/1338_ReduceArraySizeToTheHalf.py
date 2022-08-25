class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        len_remove = len(arr) / 2

        count_tbl: dict[int, int] = dict()
        for num in arr:
            count_tbl[num] = count_tbl.get(num, 0) + 1

        count = list(count_tbl.values())
        count.sort(reverse=True)

        idx, prefix = 0, 0
        while prefix < len_remove:
            prefix += count[idx]
            idx += 1
        return idx


def test_min_set_size():
    assert Solution().minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]) == 2
    assert Solution().minSetSize([7, 7, 7, 7, 7, 7]) == 1
    assert Solution().minSetSize([1, 9]) == 1
