from utils.binary_tree import TreeNode, to_tree


class BSTIterator:
    def __init__(self, root: TreeNode | None) -> None:
        self.stack = list()
        self.push_all(root)

    def next(self) -> int:
        tmp = self.stack.pop()
        self.push_all(tmp.right)
        return tmp.val

    def hasNext(self) -> bool:
        return bool(self.stack)

    def push_all(self, root):
        while root:
            self.stack.append(root)
            root = root.left


def test_bstiterator():
    obj = BSTIterator(to_tree([7, 3, 15, None, None, 9, 20]))
    assert obj.next() == 3
    assert obj.next() == 7
    assert obj.hasNext() is True
    assert obj.next() == 9
    assert obj.hasNext() is True
    assert obj.next() == 15
    assert obj.hasNext() is True
    assert obj.next() == 20
    assert obj.hasNext() is False
