from utils.binary_tree import TreeNode, to_tree


class BSTIterator:
    def __init__(self, root: TreeNode | None) -> None:
        def inorder(root: TreeNode | None) -> list[int]:
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        inorder = inorder(root)
        self.inorder_iter = iter(inorder)
        self.length = len(inorder)
        self.count = 0

    def next(self) -> int:
        self.count += 1
        return next(self.inorder_iter)

    def hasNext(self) -> bool:
        if self.count < self.length:
            return True
        else:
            return False


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
