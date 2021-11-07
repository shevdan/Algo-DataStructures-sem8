
def solve(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    self.cur_max = []
    self.max_count = 0
    self.cur = None
    self.count = 0
    def inorder(root):
        if root:
            inorder(root.left)
            if(self.cur == root.val):
                self.count += 1
                if self.count == self.max_count:
                    self.cur_max.append(self.cur)
                elif self.count > self.max_count:
                    self.cur_max = [self.cur]
                    self.max_count = self.count
            else:
                self.cur = root.val
                self.count = 1
                if self.count == self.max_count:
                    self.cur_max.append(self.cur)
                elif self.count > self.max_count:
                    self.cur_max = [self.cur]
                    self.max_count = self.count
            inorder(root.right)
    inorder(root)
    return self.cur_max
        