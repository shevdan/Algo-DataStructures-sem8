class Node:
    def __init__(self, data, left=None, right=None, parent=None) -> None:
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

class BST:
    def __init__(self) -> None:
        self.root = None
        self.size = 0


    def is_empty(self):
        return self.root is None

    def inorder(self):
        nodes_lst = []
        
        def recurse(node):
            if node is not None:
                recurse(node.left)
                nodes_lst.append(node.data)
                recurse(node.right)
        
        recurse(self.root)
        return iter(nodes_lst)
    
    def search(self, val):

        def recurse(node):
            if node is None or node.data == val:
                return node
            if val > node.data:
                return recurse(node.right)
            if val < node.data:
                return recurse(node.left)
            
        return recurse(self.root)

    def iterative_search(self, val):
        if self.root is None or self.root.data == val:
            return self.root
        node = self.root
        while node is not None and node.data != val:
            if val > node.data:
                node = node.right
            if val < node.data:
                node = node.left
            if val == node.data:
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

    def successor_node(self, item):
        
        if item.right:
            return self.node_min(item.right)
        
        
        return y

    def insert(self, val):
        node_insert = Node(val)
        node = self.root
        parent = None
        while node is not None:
            parent = node
            if val > node.data:
                node = node.right
            else:
                node = node.left

        node_insert.parent = parent
        if parent is None:
            self.root = node_insert
        elif val < parent.data:
            parent.left = node_insert
        else:
            parent.right = node_insert

        self.size += 1
    
    def delete_node(self, node_to_del):

        if node_to_del.left is None or node_to_del.right is None:
            swap_node = node_to_del
        else:
            swap_node = self.successor(node_to_del)
        if swap_node.left is not None:
            child = swap_node.left
        else:
            child = swap_node.right
        
        if child is not None:
            child.parent = swap_node.parent
        if swap_node.parent is None:
            self.root = child
        elif swap_node.parent.left == swap_node:
            swap_node.parent.left = child
        else:
            swap_node.parent.right = child
        
        if not (swap_node == node_to_del):
            node_to_del.data = swap_node.data
        
    def del_data(self, data):
        node_to_del = self.search(data)
        self.delete_node(node_to_del)

if __name__ == "__main__":
    bst = BST()
    bst.insert(1)
    bst.insert(2)
   
    bst.insert(5)
    bst.insert(3)
    bst.insert(4)


    bst.del_data(3)


    for elm in bst.inorder():
        print(elm)


        

        




