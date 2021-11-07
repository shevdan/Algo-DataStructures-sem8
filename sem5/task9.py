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
            if node.val == val:
                return
            if val > node.val:
                if node.right:
                    return recurse(node.right, val)
                node.right = TreeNode(val)
                return
            if val < node.val:
                if node.left:
                    return recurse(node.left, val)
                node.left = TreeNode(val)
                return
            
        recurse(self.root, val)
            
    def from_lst(self, lst):
        for itm in lst:
            self.insert(itm)
    
    # def delete_node(self, node_to_del):

    #     if node_to_del.left is None or node_to_del.right is None:
    #         swap_node = node_to_del
    #     else:
    #         swap_node = self.successor(node_to_del)
    #     if swap_node.left is not None:
    #         child = swap_node.left
    #     else:
    #         child = swap_node.right
        
    #     if child is not None:
    #         child.parent = swap_node.parent
    #     if swap_node.parent is None:
    #         self.root = child
    #     elif swap_node.parent.left == swap_node:
    #         swap_node.parent.left = child
    #     else:
    #         swap_node.parent.right = child
        
    #     if not (swap_node == node_to_del):
    #         node_to_del.val = swap_node.val
        
    # def del_val(self, val):
    #     node_to_del = self.search(val)
    #     self.delete_node(node_to_del)


def solve(root: TreeNode):
    max_bst = [0]

    def recurse(node):
        """
        Recursively go throught subtree, find max val in left subtree
        and min value in right subtree and check if they fall for
        bst rules - left subtree is less than root, right is bigger than root
        if true - subtree is bst
        """
        if node is None:
            return 0, True, -10**5, 10**5
        subtree_l, is_bst_l, max_left_l, min_right_l= recurse(node.left)
        subtree_r, is_bst_r, max_left_r, min_right_r = recurse(node.right)
        if is_bst_l:
            max_bst[0] = max(max_bst[0], subtree_l)
        if is_bst_r:
            max_bst[0] = max(max_bst[0], subtree_r)
        if is_bst_l and is_bst_r:
            if max_left_l < node.val < min_right_r:
                curr_sum = node.val + subtree_l + subtree_r
                max_bst[0] = max(max_bst[0], curr_sum)
                return curr_sum, True, max(max_left_l, max(node.val, max_left_r)), min(node.val, min(min_right_r, min_right_l))
        return 0, False, -10**5, 10**5

    recurse(root)
    return max_bst[0]



if __name__ == "__main__":
    bst = BST()
    # bst.insert(1)
    # bst.insert(2)
   
    # bst.insert(5)
    # bst.insert(3)
    # bst.insert(4)
    root = [1,4,3,2,4,2,5,None,None,None,None,None,None,4,6]
    bst.from_lst(root)



    for elm in bst.inorder():
        print(elm)
        print(solve(bst.root))