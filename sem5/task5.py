class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deleteZeroes(root:TreeNode):
    if root:
        rightEmpty = True
        leftEmpty = True
        if root.right:
            rightEmpty = deleteZeroes(root.right)
        if root.left:
            leftEmpty = deleteZeroes(root.left)
        if rightEmpty:
            root.right = None
        if leftEmpty:
            root.left = None
        return root.val == 0 and rightEmpty and leftEmpty
    return True

rootRightRight = TreeNode(0)
rootRightLeft = TreeNode(0)
rootRight = TreeNode(0,rootRightLeft,rootRightRight)
rootLeftRight = TreeNode(0)
rootLeftLeft = TreeNode(0)
rootLeft = TreeNode(1, rootLeftLeft, rootLeftRight)
root = TreeNode(0,rootLeft,rootRight)
deleteZeroes(root)

print(root.val, root.left.val, root.right, root.left.left,root.left.right)