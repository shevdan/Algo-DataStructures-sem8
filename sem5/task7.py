
class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self) -> None:
        self.root = None

    def max_sum(self):
        sum = [0]

        def recurse(node):
            if node is None:
                return 0
            max_left = recurse(node.left)
            max_right = recurse(node.right)
            sub_tree = node.val + max_left + max_right
            sum[0] = max(sum[0], sub_tree)
            return sub_tree
        
        recurse(self.root)
        return sum[0]


    def is_empty(self):
        return self.root is None

    def inorder(self):
        nodes_lst = []
        
        def recurse(node):
            if node is not None:
                recurse(node.left)
                nodes_lst.append(node.val)
                recurse(node.right)
        
        recurse(self.root)
        return iter(nodes_lst)
    
    def search(self, val):

        def recurse(node):
            if node is None or node.val == val:
                return node
            if val > node.val:
                return recurse(node.right)
            if val < node.val:
                return recurse(node.left)
            
        return recurse(self.root)

    def iterative_search(self, val):
        if self.root is None or self.root.val == val:
            return self.root
        node = self.root
        while node is not None and node.val != val:
            if val > node.val:
                node = node.right
            if val < node.val:
                node = node.left
            if val == node.val:
                return node


        return node
    
    def node_min(self, node):
        while node.left is not None:
            node = node.left
        
        return node
    
    def node_max(self, node):
        while node.right is not None:
            node = node.right
        
        return node

    def bst_min(self):
        if self.root is None:
            return self.root
        
        return self.node_min(self.root)

    def bst_min(self):
        if self.root is None:
            return self.root
        
        return self.node_max(self.root)

    # def successor_node(self, item):
        
    #     if item.right:
    #         return self.node_min(item.right)
        
        
    #     return y

    def insert(self, val):
        if val is None:
            return
        
        if self.root is None:
            self.root = TreeNode(val)
            return

        def recurse(node, val):
            if val >= node.val:
                if node.right:
                    return recurse(node.right, val)
                node.right = TreeNode(val)
                return
            if val <= node.val:
                if node.left:
                    return recurse(node.left, val)
                node.left = TreeNode(val)
                return
            
        recurse(self.root, val)
            
    def from_lst(self, lst):
        for itm in lst:
            self.insert(itm)


class Sol:
    def solve(self, root):
        self.curr_max = []
        self.max_count = 0
        self.cur = None
        self.count = 0


        def recurse(node):
            if node:

                recurse(node.left)

                if self.cur == node.val:
                    if self.cur == node.val:
                        self.count += 1
                    if self.count == self.max_count:
                        self.curr_max.append(self.cur)
                    elif self.count > self.max_count:
                        self.curr_max = [self.cur]
                        self.max_count = self.count
                else:
                    self.cur = node.val
                    self.count = 1
                    if self.count == self.max_count:
                        self.curr_max.append(self.curr_max)
                    elif self.count > self.max_count:
                        self.curr_max = [self.cur]
                        self.max_count = self.count
                recurse(node.right)
        
        recurse(root)
        return self.curr_max

                
