
def solve(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    self.sum = 0
    def inreverse(root):
        if root:
            inreverse(root.right)
            root.val += self.sum
            self.sum = root.val
            inreverse(root.left)
    inreverse(root)
    return root
            
        