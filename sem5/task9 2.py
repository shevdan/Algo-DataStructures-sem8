def solve(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.maxSum = float("-inf")
    # we need to keep track if the bst is correct and of the sum
    # for this the max sum is stored in self and helper method will return
    # sum, mux, min for a subtrre and bool value (true if subtree is correct BST)
    def helper(root):
        if root:
            rightIsBST, rightMin, rightMax, rightSum = helper(root.right)
            leftIsBST, leftMin, leftMax, leftSum = helper(root.left)
            if rightIsBST and leftIsBST and leftMax<root.val<rightMin:
                self.maxSum = max(root.val+rightSum+leftSum, self.maxSum)
                return True, min(leftMin,root.val), max(rightMax,root.val), root.val+rightSum+leftSum
            return False, -1,-1, -1
        #null(after leaf node) is always BST(True), to avoid conflicts with values we set min to inf and
        #max to -inf. The sum is 0
        return True, float("inf"), float("-inf"), 0
    helper(root)
    return max(self.maxSum,0)
            