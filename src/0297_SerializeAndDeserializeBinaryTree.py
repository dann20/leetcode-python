from utils.binary_tree import TreeNode, to_tree


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        if not root:
            return ""
        new_level = []
        cur_level = [root]
        res = []
        while any(cur_level):
            res.append([])
            for node in cur_level:
                if node:
                    res[-1].append(node.val)
                    new_level.append(node.left)
                    new_level.append(node.right)
                else:
                    res[-1].append(node)
            cur_level = new_level
            new_level = []

        res = [",".join([str(num) if num is not None else "n" for num in level]) for level in res]
        return " ".join(res)

    def deserialize(self, data: str) -> TreeNode | None:
        if not data:
            return None

        data = data.split(" ")
        data = [level.split(",") for level in data]
        data = [[int(num) if num != "n" else None for num in level] for level in data]

        root = TreeNode(data[0][0])
        cur_level = [root]

        for level in data[1:]:
            new_level = [TreeNode(val) if val is not None else None for val in level]
            for idx, node in enumerate(cur_level):
                node.left = new_level[2 * idx]
                node.right = new_level[2 * idx + 1]
            cur_level = [node for node in new_level if node]

        return root


def test_codec():
    codec = Codec()
    root = to_tree([1, 2, 3, 7, 8, 4, 5, None, None, None, None, None, 6, None, None, 10, 11, 12, None])

    str_tree = codec.serialize(root)
    assert str_tree == "1 2,3 7,8,4,5 n,n,n,n,n,6,n,n 10,11 12,n,n,n"

    ans = codec.deserialize(str_tree)
    assert ans == root

    root2 = to_tree([0, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None,
                    -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1, -4, None, None, None, -2, None])

    str_tree_2 = codec.serialize(root2)
    assert str_tree_2 == "0 -7,-3 n,n,-9,-3 9,-7,-4,n 6,n,-6,-6,n,n 0,6,5,n,9,n n,-1,-4,n,n,n,-2,n"

    ans_2 = codec.deserialize(str_tree_2)
    assert ans_2 == root2
